import os
import numpy as np
import base64
import json
import math
import datetime
import pandas as pd

import helper.log_helper as log_helper

# Define Logger without file handle
logger = log_helper.get(False, "Data Parse")


class DataParser:
    def parse_input_data(self, file_path, calibration=True, custom_offset=0):
        """
        Parses a JSON
        :param file_path:   path to the JSON file
        :param direct_json: pass JSON directly
        :param calibration: if True, acceleration data will be calibrated
        :param custom_offset: returns the angle,offset,force etc. for the specified offset in ms {default: 0 = max force}
        :return:    (angle in degrees, offset to max force value in ms, relative max force, list of all force values)
        """
        base_json = self.__read_json_from_filesystem(file_path)
        b64payload = self.__get_b64payload_from_basejson(base_json)
        encoded = self.__base64_decode(b64payload)
        pylist = self.__encoded_payload_to_list(encoded)

        predicted_impact_time = pylist["data"][pylist["pos"]][0]

        acceleration = pylist["data"]
        acceleration = sorted(acceleration, key=lambda d: d[0])

        acceleration = np.array(acceleration)

        # get rel_times for better handlin
        rel_time = acceleration[:, 0]
        # get x,y,z for better handling
        acceleration = acceleration[:, 1:]

        if calibration:
            acceleration = self.calibrate_impact_data(acceleration[:, 0], acceleration[:, 1], acceleration[:, 2],
                                                      pylist['calibration'])

        # norm with oneG
        one_g = pylist["oneG"]
        # norm with one g
        acceleration = self.__norm_with_g(acceleration, one_g)
        damage_id = pylist["id"]


        if custom_offset != 0:  # calculate custom offset force
            #custom_offset = np.min(rel_time) + custom_offset
            max_force_offset = custom_offset
            index = int(custom_offset / 16000 * acceleration.shape[0])
            # get index of offset
            #index = np.where(rel_time == max_force_offset)
            max_force = self.__calculate_custom_offset_force(index, acceleration)
            print(max_force)
        else:  # calculate max offset
            max_force_offset = self.__calculate_offset_max_force(rel_time, acceleration)
            max_force = self.__calculate_max_force(acceleration)
            index = np.where(rel_time == max_force_offset)

        crash_time = pylist["timestamp"]
        crash_time = pd.to_datetime(crash_time, unit='s')

        # calculate angle
        angle_impact = self.__calculate_angle(index, predicted_impact_time, rel_time, acceleration[:, 0],
                                              acceleration[:, 1])

        return angle_impact, max_force, damage_id, crash_time, max_force_offset

    def get_rel_times(self, jsonfile):
        """Liefert die Rel-Timestamps des Datensatzes zurück

        Arguments:
            json {[type]} -- Crash Json

        Return:
            list -- rel-times
        """
        base_json = self.__read_json_from_filesystem(jsonfile)
        b64payload = self.__get_b64payload_from_basejson(base_json)
        encoded = self.__base64_decode(b64payload)
        pylist = self.__encoded_payload_to_list(encoded)
        acceleration = pylist["data"]
        acceleration = sorted(acceleration, key=lambda d: d[0])
        acceleration = self.__get_virtual_xyz(pylist['data'], pylist['calibration'])
        rel_time = [x[0] for x in acceleration]
        return rel_time

    def __base64_decode(self, base64_string):
        """
        Decodes a base64 encoded string to a UTF-8 string.
        :param base64_string:    base64 string
        :return:                 decoded character string
        """

        # Decode string
        decoded_string = base64.b64decode(base64_string)
        decoded_string = decoded_string.decode("utf-8")

        return decoded_string

    def __convert_timestamps(self, data, timestamp, reference_time):
        """
        Converts the relative timestamps of the accelerometer data array to absolute timestamps.
        :param data:            raw data from the accelerometer component
        :param timestamp:       real time unix timestamp in seconds since epoch
        :param reference_time:  reference timestamp in seconds for converting data timestamp to real timestamp
        :return:                data array with converted timestamps
        """
        array = np.array(data)
        array = array.astype(np.uint64)
        c = (timestamp - reference_time) * 1000
        array[:, 0] = array[:, 0] + c
        return array.tolist()

    @DeprecationWarning
    def __get_virtual_xyz(self, acceleration, calibration):
        """Calibrates virtual x,y,z data from the acceleration and calibration (0 used)
        :param acceleration:    data array with [ [timestamp, x, y, z], [...], ...]
        :param calibration:     calibrations array like [ [x,y,z] , [x2,y2,z2], [x3,y3,z3] ]
        :return:                Virtual position array like [ [timestamp, virt_x, virt_y, virt_z], ...]
        """

        for i_acc in acceleration:
            virt_x = calibration[0][0] * i_acc[1] + calibration[0][1] * i_acc[2] + calibration[0][2] * i_acc[3]
            i_acc[1] = virt_x
            virt_y = calibration[1][0] * i_acc[1] + calibration[1][1] * i_acc[2] + calibration[1][2] * i_acc[3]
            i_acc[2] = virt_y
            virt_z = calibration[2][0] * i_acc[1] + calibration[2][1] * i_acc[2] + calibration[2][2] * i_acc[3]
            i_acc[3] = virt_z
        return acceleration

    def calibrate_impact_data(self, rx, ry, rz, calibration):
        """Use the calibration data to calibrate the given data."""
        calibrated_rx = [calibration[0][0] * x + calibration[0][1] * y + calibration[0][2] * z for x, y, z in
                         zip(rx, ry, rz)]
        calibrated_ry = [calibration[1][0] * x + calibration[1][1] * y + calibration[1][2] * z for x, y, z in
                         zip(rx, ry, rz)]
        calibrated_rz = [calibration[2][0] * x + calibration[2][1] * y + calibration[2][2] * z for x, y, z in
                         zip(rx, ry, rz)]

        return np.column_stack((calibrated_rx, calibrated_ry, calibrated_rz))

    def __norm_with_g(self, acceleration, one_g):
        return acceleration / one_g

    # only force calc
    def __calculate_forces(self, acceleration):
        forces = np.square(acceleration)
        forces = np.sum(forces, axis=1)
        return np.sqrt(forces)

    # not directly
    def __calculate_max_force(self, acceleration):
        forces = self.__calculate_forces(acceleration)
        return np.max(forces)

    def __calculate_offset_max_force(self, rel_time, acceleration):
        forces = self.__calculate_forces(acceleration)
        offset_max_force = np.argmax(forces)  # index of max force value
        return rel_time[offset_max_force]  # relative time at max force value

    def __calculate_custom_offset_force(self, custom_offset, acceleration):
        return np.sqrt(np.square(acceleration[custom_offset,:]).sum())

    def __calculate_angle(self, index, predicted_impact_time, rel_time, rx, ry):
        return 180 - math.degrees(np.arctan2(ry[index], rx[index]))

    def __ringbuffer2array(self, ringbuffer):
        """
        Sorts ringbuffer into an array.
        The ringbuffer contains data in form of an array, of which the first value is the timestamp.
        :param ringbuffer:  raw data from the accelerometer component
        :return:            data sorted by timestamp
        """
        rb = np.array(ringbuffer)
        return rb[rb[:, 0].argsort()]

    def __read_json_from_filesystem(self, path2file):
        if len(path2file) < 255 and os.path.exists(path2file):
            with open(path2file) as json_file:
                data = json.load(json_file)
                return data

        if type(path2file) is str:
            return json.loads(path2file)

        return None

    def __get_b64payload_from_basejson(self, base_json):
        return base_json[0]['payload']['b64_payload']

    def __encoded_payload_to_list(self, encodedjsonstring):
        return json.loads(encodedjsonstring)
