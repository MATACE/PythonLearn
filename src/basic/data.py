#!/bin/usr/python
# coding=utf-8

import logging


def y_run():
    yun = {"greed":32, "good": 56}
    for i in yun.keys():
        print(i)
    for i in yun.items():
        print(i)
    for i in yun.values():
        print(i)
    if "greed" in yun.keys():
        print("Ok")
    if yun.get("greed", 0) == 0:
        print("not Find")

def show_name(name):
    name = "abc"
    name = "xyz"

def run():
    name = "fpsxyz"
    if name.endswith("z"):
        logging.info("OK")