import numpy as np
import pandas as pd
import base64

from helper import log_helper
#Definde Logger without Filehandle
logger = log_helper.get(False, "Data Parse")



class DataParser:
    def parse_input_data(self, data):
        object = None
        # TODO implment
        return object

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

    def __real_acceleration(self, acceleration, calibration):
        """
        Calibrates acceleration data
        :param acceleration:
        :param calibration:
        :return:
        """
        # TODO implement DAVE

    def __ringbuffer2array(self, ringbuffer):
        """
        Sorts ringbuffer into an array.
        The ringbuffer contains data in form of an array, of which the first value is the timestamp.
        :param ringbuffer:
        :return:
        """
        # TODO implement SERGE

        