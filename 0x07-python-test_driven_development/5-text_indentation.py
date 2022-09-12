#!/usr/bin/python3
def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    line_list = []
    starting = True
    for idx in range(0, len(text)):
        if text[idx] == " " and starting is True:
            idx += 1
            continue
        if text[idx] == "." or text[idx] == "?" or text[idx] == ":":
            print("{}\n".format(text[idx]))
            starting = True
        else:
            print(text[idx], end='')
            starting = False
    print("\n")
