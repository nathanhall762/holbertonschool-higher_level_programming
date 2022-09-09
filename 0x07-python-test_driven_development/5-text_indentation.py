#!/usr/bin/python3
def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    line_list = []
    for idx in range(0, len(text)):
        if text[idx] == "." or text[idx] == "?" or text[idx] == ":":
            #print("{}\n".format(text[idx]))
            line_list.append(text[idx])
            print(*line_list, sep='')
            line_list = []
        else:
            #print(text[idx], end='')
            line_list.append(text[idx])
    print("\n")

#this shit is totally fucked. redo logic because space at beginning of line is a nogo.