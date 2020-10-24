#!/usr/bin/python
#coding=utf-8

import logging
from logging import disable, log, logMultiprocessing

class LogOp():
    def __init__(self) -> None:
        pass
    
    def config_log(self, log_level, log_file_name="", log_file_mode="w+"):
        """ Set the logging level and log file name.

        Args:
            log_level (string): [description]
            log_file_name (string, ""): The save log file name. Defaults to "".
            log_file_mode (string, "w+"): The log file save mode. Defaults to "w+".
        """
        if log_file_name == None:
            logging.basicConfig(log_level,\
                format='%(levelname)s %(asctime)s [%(filename)s:%(lineno)d] %(message)s',\
                datefmt='%Y.%m.%d. %H:%M:%S'\
                )
        else:
            logging.basicConfig(log_level,\
                format='%(levelname)s %(asctime)s [%(filename)s:%(lineno)d] %(message)s',\
                datefmt='%Y.%m.%d. %H:%M:%S',\
                log_file_name='parser_result.log',
                filemode=log_file_mode
                )
    def disable_log(self, disable_level = "ERROR"):
        logging.disable(disable_level)


