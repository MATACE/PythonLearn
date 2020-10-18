#!/bin/bash
# -*- coding: UTF-8 -*-

def show_p():
    print("This is show p")

def show_m():
    i = 3 ** 2
    print(i)

def show_s():
    str = 'Bye' * 3
    print(str)

def get_n():
    print("Input your name:")
    your_name = input()
    print("Good see you: " + your_name)
    print("Your name len: " + str(len(your_name)))
    print("Your age: ")
    age = input()
    print("Your age: " + age)
    print('Bye ' * 2)

def my_add():
    i = input()
    j = input()
    print(int(i) + int(j))

def main():
    my_add()

