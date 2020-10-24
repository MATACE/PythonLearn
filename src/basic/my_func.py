#!/bin/usr/python
# coding=utf-8

import sys

def run_3():
    """
    @param: jife
    @return: jfieji
    """
    str = """
    1.one # one
    2.two # two
    3.three # three
    """
    print(str)

def run_1():
    str = 'test1'
    str1 = ' test1 "Hello"'
    print(str + str1)

def run_2():
    str = "test2"
    str1 = " test2 'Hello'"
    print(str + str1)

def add_name():
    name = input()
    if name == "joy":
        print("ok")
    else:
        print("no ok")

def name_len(name):
    print(name)
    return len(name)

glb_n = 0
def my_p():
    global glb_n
    print(glb_n)
    glb_n += 1
    print(glb_n)

def my_zero(num):
    try:
        value = 10 / num
    except ZeroDivisionError:
        print(num)

def my_array():
    array = ["dog", "cat", "milk"]
    tol_n = 0
    for tol_n in range(0, 3):
        print(array[tol_n])
    print(array[-1])

def f_array():
    array = ["dog", "cat", "pig", "milk"]
    array1 = array
    print(array1[:2])
    print(array[1:-1])

def add_array():
    array1 = ["dog", "cat", "pig", "milk"]
    array2 = ["abc", "bcd", "edf"]
    array3 = array1 + array2
    del array3[0];
    print(array3)

def my_in():
    array1 = ["mac", "ipad"]
    print("dog" in array1)

def op_array():
    array1 = ["abc", "def", "fps"]
    array1.append("123")
    array1.insert(0, "fpm")
    array1.remove("fps")
    array1.sort()
    print(array1)

def show_test():
    array = ["abc", "lsp", "mni"]
    print(tuple(array))
    yun = ("123", "xyz", "mnt")
    print(list("abc"))

import copy
def my_copy(array):
    array[0] = "123"
    my_array = copy.copy(array)
    my_array[0] = "abc"
    print(my_array)

def run():
    array = ["fps"]
    my_copy(array)
    print(array)
