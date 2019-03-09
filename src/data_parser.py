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

        #conver realtive times from data and from gps data
        #ToDo
        #get virtual xyz into payload

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

    def __relative2absolute_timestamp(self, relative_timestamp, timestamp, reference_time):
        """
        Converts the relative timestamp to an absolute timestamp.
        :param relative_timestamp:
        :param timestamp:
        :param reference_time:
        :return:    absolute timestamp
        """
        # TODO implement SERGE

    def __get_virtual_xyz(self, acceleration, calibration):
        """
        Calibrates virutal x,y,z data from the acceleration and calibration (0 used)

        :param acceleration:    array like [x,y,z]
        :param calibration:     array like [ [x,y,z] , [x2,y2,z2], [x3,y3,z3] ]
        :return:                Virtual position array like [virt_x, virt_y, virt_z]
        """
        #acceleration: Sensor value
        #calibration:calibration known at crash
        #Use the calibration matrix to potentially compute the virtual x,y,z values
        # x = calibration[0][0] * rx + calibration[0][1] * ry + calibration [0][2] * rz
        #also, rx,ry,rz sind nur beschleunigungen, mit der Kalibration erhält man die Position

        #Check if arrays correct
        if(len(acceleration) !=3 | len(calibration)!=3 ):
            logger.error("Acceleration oder Calibration Data incorrect (not size 3)")
            return
        #Check sub array calibration
        for i in range (3):
            if(len(calibration[i]) != 3):
                logger.error("Sub item %i in Calibration is incorrect", i)

        #Convert to Virtual Positon
        virt_x = calibration[0][0] * acceleration[0] + calibration[0][1] * acceleration[1] + calibration[0][2] * acceleration[2] 
        virt_y = calibration[1][0] * acceleration[0] + calibration[1][1] * acceleration[1] + calibration[1][2] * acceleration[2] 
        virt_z = calibration[2][0] * acceleration[0] + calibration[2][1] * acceleration[1] + calibration[2][2] * acceleration[2] 
        logger.info("x: %d",virt_x)
        logger.info("y: %d",virt_y)
        logger.info("z: %d",virt_z)

        return [virt_x, virt_y, virt_z]


    def __ringbuffer2array(self, ringbuffer):
        """
        Sorts ringbuffer into an array.
        The ringbuffer contains data in form of an array, of which the first value is the timestamp.
        :param ringbuffer:
        :return:
        """
        # TODO implement SERGE

    def __read_json_from_filesystem(self, path2file):
        with open(path2file) as json_file:
            data = json.load(json_file)
            return data

    def __get_b64payload_from_basejson(self, basejson):
        return basejson[0]['payload']['b64_payload'] 

#read json from fs

basejson = DataParser._DataParser__read_json_from_filesystem(None, r'C:\hslu\git\starthack-asimov\src\data\encoded_b64payload_small.json')
b64payload = DataParser._DataParser__get_b64payload_from_basejson(None, basejson)    
encoded = DataParser._DataParser__base64_decode(None, b64payload)
print(encoded)
