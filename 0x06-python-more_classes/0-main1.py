#!/usr/bin/python3
Rectangle = __import__('0-rectangle').Rectangle

try:
    my_rectangle = Rectangle(2, "3")
    print("trying")
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

try:
    my_rectangle = Rectangle("2", 3)
    print("trying")
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
