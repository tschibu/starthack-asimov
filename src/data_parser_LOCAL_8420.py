import numpy as np
import pandas as pd
import base64
import json

from helper import log_helper
#Definde Logger without Filehandle
logger = log_helper.get(False, "Data Parse")



class DataParser:
    def parse_input_data(self, data):
        object = None
        # TODO implment
        #ablauf
        # decode base64
        payload = DataParser.__base64_decode(self,data)
        # the json into an array structure
        payload_arr  = json.loads(payload)

        #1 order ringbuffer
        #2 add relative time to data
        #3 add virtual xyz to data

        #convert relative times from data and from gps data
        #ToDo

        #return finishes json with real time and xyz
        return payload_arr_done

    def __base64_decode(self, base64_string):
        """
        Decodes a base64 encoded string to a UTF-8 string.
        :param base64_string:    base64 string
        :return:                 decoded character string
        """
        logger.info("Base64 Encoding string")

        #Decode string
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
        array[:, 0] = (timestamp - reference_time) * 1000 + array[:, 0]
        return array


    def __relative2absolute_timestamp(self, relative_timestamp, timestamp, reference_time):
        """
        Converts the relative timestamp to an absolute timestamp.
        :param relative_timestamp:  relative timestamp in milliseconds
        :param timestamp:           real time unix timestamp in seconds since epoch
        :param reference_time:      reference timestamp in seconds for converting data timestamp to real timestamp
        :return:                    absolute timestamp
        """
        # TODO implement SERGE
        return (timestamp - reference_time) * 1000 + relative_timestamp


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

            print(i_acc[0])

            virt_x = calibration[0][0] * i_acc[1] + calibration[0][1] * i_acc[2] + calibration[0][2] * i_acc[3]
            i_acc[1] = virt_x
            logger.info("x: %d",virt_x)

            virt_y = calibration[1][0] * i_acc[1] + calibration[1][1] * i_acc[2]  + calibration[1][2] * i_acc[3]
            i_acc[2] = virt_y
            logger.info("y: %d",virt_y)

            virt_z = calibration[2][0] * i_acc[1] + calibration[2][1] * i_acc[2]  + calibration[2][2] * i_acc[3]
            i_acc[3] = virt_z
            logger.info("z: %d",virt_z)

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
        return rb[rb[:,0].argsort()]

    def __read_json_from_filesystem(self, path2file):
        with open(path2file) as json_file:
            data = json.load(json_file)
            return data

    def __get_b64payload_from_basejson(self, basejson):
        return basejson[0]['payload']['b64_payload']
    
    def __encoded_payload_to_list(self, encodedjsonstring):
        return json.loads(encodedjsonstring)

##Example Code
#basejson = DataParser._DataParser__read_json_from_filesystem(None, r'C:\hslu\git\starthack-asimov\src\data\encoded_b64payload_small.json')
basejson = DataParser._DataParser__read_json_from_filesystem(None, r'C:\hslu\git\starthack-asimov\src\data\1.json')

b64payload = DataParser._DataParser__get_b64payload_from_basejson(None, basejson)
encoded = DataParser._DataParser__base64_decode(None, b64payload)
#now convert the json encoded to a numpy array
pylist = DataParser._DataParser__encoded_payload_to_list(None, encoded)

acctest = DataParser._DataParser__get_virtual_xyz(None,pylist["data"], pylist["calibration"])
print(acctest)

import matplotlib.pyplot as plt  
#x = np.linspace(-10, 9, 20)
#y = x ** 3

#get every x and y into array

x_plt = []
y_plt = []
for i in acctest:
    x_plt.append(i[1])
    y_plt.append(i[2])



print(x_plt)
print (y_plt)

plt.scatter(x_plt, y_plt)  
plt.xlabel('X axis')  
plt.ylabel('Y axis')  
plt.title('Cube Function')  
plt.show()  