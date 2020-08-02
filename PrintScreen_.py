#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# __author__ = "10291"

import time

from PIL import ImageGrab

a = 0
while True:
    a = a + 1
    pic = ImageGrab.grab()
    pic.save("C:\\Users\\10291\\OneDrive\\picture.jpg")
    print(a + 1)
    time.sleep(60)
