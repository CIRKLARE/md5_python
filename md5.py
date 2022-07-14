#!/bin/python3
import hashlib
print('''
███╗   ███╗██████╗ ███████╗
████╗ ████║██╔══██╗██╔════╝
██╔████╔██║██║  ██║███████╗
██║╚██╔╝██║██║  ██║╚════██║
██║ ╚═╝ ██║██████╔╝███████║
╚═╝     ╚═╝╚═════╝ ╚══════╝
                           

''')
text = input("text : ")
print("md5 hash :",hashlib.md5(text.encode()).hexdigest())