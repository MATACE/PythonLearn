#!/usr/bin/python
# coding=utf-8

import logging
from src.mode1 import mode1
from src.mode2 import mode2
from src.basic import op
from src.basic import my_func
from src.basic import data
from src.log   import LogOp

def func():
    # op.main()
    # mode1.mode1()
    # mode2.mode2()

    # Init the logging
    log_op = LogOp()
    log_op.config_log(logging.DEBUG)

    data.run()
