import numpy as np
import base64
import json

from helper import log_helper
#Definde Logger without Filehandle
logger = log_helper.get(False, "Data Parse")



class DataParser:
    def parse_input_data(self, file_path):
        basejson = self.__read_json_from_filesystem(file_path)
        b64payload = self.__get_b64payload_from_basejson(basejson)
        encoded = self.__base64_decode(b64payload)
        pylist = self.__encoded_payload_to_list(encoded)
        pylist['data'] = self.__convert_timestamps(pylist['data'], pylist['timestamp'], pylist['referenceTime'])
        pylist['data'] = self.__get_virtual_xyz(pylist['data'], pylist['calibration'])
        del pylist['timestamp']
        del pylist['referenceTime']
        del pylist['calibration']
        return pylist


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
        Calibrates virutal x,y,z data from the acceleration and calibration (0 used)

        :param acceleration:    data array with [ [timestamp, x, y, z], [...], ...]
        :param calibration:     calibrations array like [ [x,y,z] , [x2,y2,z2], [x3,y3,z3] ]
        :return:                Virtual position array like [ [timestamp, virt_x, virt_y, virt_z], ...]
        """
        #acceleration: Sensor value
        #calibration:calibration known at crash
        #Use the calibration matrix to potentially compute the virtual x,y,z values
        # x = calibration[0][0] * rx + calibration[0][1] * ry + calibration [0][2] * rz
        #also, rx,ry,rz sind nur beschleunigungen, mit der Kalibration erhält man die Position

        for i_acc in acceleration:
            virt_x = calibration[0][0] * i_acc[1] + calibration[0][1] * i_acc[2] + calibration[0][2] * i_acc[3]
            i_acc[1] = virt_x
            #logger.info("x: %d",virt_x)

            virt_y = calibration[1][0] * i_acc[1] + calibration[1][1] * i_acc[2]  + calibration[1][2] * i_acc[3]
            i_acc[2] = virt_y
            #logger.info("y: %d",virt_y)

            virt_z = calibration[2][0] * i_acc[1] + calibration[2][1] * i_acc[2]  + calibration[2][2] * i_acc[3]
            i_acc[3] = virt_z
            #logger.info("z: %d",virt_z)

        return acceleration


    def __ringbuffer2array(self, ringbuffer):
        """
        Sorts ringbuffer into an array.
        The ringbuffer contains data in form of an array, of which the first value is the timestamp.
        :param ringbuffer:  raw data from the accelerometer component
        :return:            data sorted by timestamp
        """
        # TODO implement SERGE
        rb = np.array(ringbuffer)
        return rb[rb[:, 0].argsort()]

    def __read_json_from_filesystem(self, path2file):
        with open(path2file) as json_file:
            data = json.load(json_file)
            return data

    def __get_b64payload_from_basejson(self, basejson):
        return basejson[0]['payload']['b64_payload']
    
    def __encoded_payload_to_list(self, encodedjsonstring):
        return json.loads(encodedjsonstring)

dp = DataParser()
result = dp.parse_input_data(r'C:\hslu\git\starthack-asimov\src\data\2.json')
print(result)