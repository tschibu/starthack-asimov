import numpy as np
import pandas as pd
import json

class DataParser:
    def parse_input_data(self, data):
        print("éSJDFKLéSJéDLFK")
        print(data)
        object = json.loads(data)
        # TODO implment
        print("éSJDFKLéSJéDLFK")
        print(object)
        return object

    def __base64_decode(self, base64_string):
        """
        Decodes a base64 encoded string to a UTF-8 string.
        :param base64_string:    base64 string
        :return:                 decoded character string
        """
        # TODO implement DAVE

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
        :param ringbuffer:  raw data from the accelerometer component
        :return:            data sorted by timestamp
        """
        # TODO implement SERGE
        rb = np.array(ringbuffer)
        return rb[rb[:,0].argsort()]
