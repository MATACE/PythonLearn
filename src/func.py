#!/usr/bin/python
# coding=utf-8

import logging
from src.mode1 import mode1
from src.mode2 import mode2
from src.basic import op
from src.basic import my_func
from src.basic import data
from src.log   import LogOp
from src.web.web_op import WebOp
from src.excel.excel_op import ExcelOp

def func():
    # op.main()
    # mode1.mode1()
    # mode2.mode2()

    # Init the logging
    log_op = LogOp()
    log_op.config_log(logging.DEBUG)

    excel_op = ExcelOp()
    # excel_op.open()
    excel_op.create_grap()

    # data.run()
