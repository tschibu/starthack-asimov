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
    def parse_input_data(self, file_path, calibration=True):
        """
        Parses a JSON
        :param file_path:   path to the JSON file
        :param direct_json: pass JSON directly
        :param calibration: if True, acceleration data will be calibrated
        :return:    (angle in degrees, offset to max force value in ms, relative max force, list of all force values)
        """
        base_json = self.__read_json_from_filesystem(file_path)
        b64payload = self.__get_b64payload_from_basejson(base_json)

        b64payload = self.__get_b64payload_from_basejson(base_json)

        encoded = self.__base64_decode(b64payload)
        # convert to python list
        pylist = self.__encoded_payload_to_list(encoded)

        predicted_impact_time = pylist["data"][pylist["pos"]][0]

        acceleration = pylist["data"]
        acceleration = sorted(acceleration, key=lambda d: d[0])

        if calibration:
            acceleration = self.__get_virtual_xyz(pylist['data'], pylist['calibration'])

        # norm with oneG
        oneG = pylist["oneG"]
        damage_id = pylist["id"]

        rel_time = [x[0] for x in acceleration]
        rx = [x[1] for x in acceleration]
        ry = [x[2] for x in acceleration]
        rz = [x[3] for x in acceleration]

        # calculate forces
        forces = self.__calculate_forces(rx, ry, rz)
        max_force_offset = self.__calculate_offset_max_force(rel_time, rx, ry, rz)
        max_force = self.__calculate_max_force(rel_time, rx, ry, rz)

        crash_time = pylist["timestamp"] + max_force_offset
        crash_time = pd.to_datetime(crash_time, unit='s')

        # calculate angle
        angle_impact = self.__calculate_angle(max_force_offset, predicted_impact_time, rel_time, rx, ry)

        return angle_impact, max_force, damage_id, crash_time, max_force_offset

    def __base64_decode(self, base64_string):
        """
        Decodes a base64 encoded string to a UTF-8 string.
        :param base64_string:    base64 string
        :return:                 decoded character string
        """
        logger.info("Base64 Encoding string")

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

    def __get_virtual_xyz(self, acceleration, calibration):
        """
        Calibrates virtual x,y,z data from the acceleration and calibration (0 used)

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

    def __norm_with_g(self, acceleration, one_g):
        for n_acc in acceleration:
            n_acc[1] = n_acc[1] / one_g
            n_acc[2] = n_acc[2] / one_g
            n_acc[3] = n_acc[3] / one_g
        return acceleration

    # only force calc
    def __calculate_forces(self, rx, ry, rz):
        return [np.sqrt(x ** 2 + y ** 2 + z ** 2) for x, y, z in zip(rx, ry, rz)]

    # not directly
    def __calculate_max_force(self, rel_time, rx, ry, rz):
        forces = self.__calculate_forces(rx, ry, rz)
        return np.max(forces)

    def __calculate_offset_max_force(self, rel_time, rx, ry, rz):
        forces = self.__calculate_forces(rx, ry, rz)
        offset_max_force = forces.index(np.max(forces))  # index of max force value
        return rel_time[offset_max_force]  # relative time at max force value

    def __calculate_angle(self, offset_maxforce_in_ms, predicted_impact_time, rel_time, rx, ry):
        try:
            offset_index = rel_time.index(offset_maxforce_in_ms)
        except ValueError:
            return None

        if offset_maxforce_in_ms - predicted_impact_time <= 0:
            return None
            logger.error("Impact should be in the future, black magic")

        return 180 - math.degrees(np.arctan2(ry[offset_index], rx[offset_index]))

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
        with open(path2file) as json_file:
            data = json.load(json_file)
            return data

    def __get_b64payload_from_basejson(self, base_json):
        return base_json[0]['payload']['b64_payload']

    def __encoded_payload_to_list(self, encodedjsonstring):
        return json.loads(encodedjsonstring)

# dp = DataParser()
# result = dp.parse_input_data(r'C:\hslu\git\starthack-asimov\src\data\1.json')
# print(result)
