"""[Log Helper]

Helper class to instantinate loggers
"""

import logging

def get(fileHandler=False, logger_name="undefined"):
    """[Creates Logger]

    Keyword Arguments:
        fileHandler {[boolean]} -- Creates filehandler (default: {FALSE})
        logger_name {str} -- Name of logger (default: {"undefined"})

    Returns:
        logging.getLogger() -- logging object
    """

    #Setting Up Logger
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)

    #Optional File Logger
    if (fileHandler):
        fh = logging.FileHandler(logger_name + "_01.log")
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(formatter)
        logger.addHandler(fh)

    logger.addHandler(ch)
    return logger