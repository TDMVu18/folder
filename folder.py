# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 21:47:39 2020

@author: LENOVO
"""

import os
folder=input("Nhập tên thư mục:")
os.mkdir(folder)
f = open('file.txt', 'w+')
f.write('Hello World')
f.close()