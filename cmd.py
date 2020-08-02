#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# __author__ = "10291"
# 读取IP地址并保存到txt文件中

import os
import subprocess
import requests
import re
import time
import xgboost as xgb


def text_create(name, msg):
    desktop_path = "C:\\Users\\10291\\OneDrive\\"  # 新创建的txt文件的存放路径
    full_path = desktop_path + name + '.txt'  # 也可以创建一个.doc的word文档
    file = open(full_path, 'a')
    file.write(msg + "\n")
    file.close()


def clear_txt():
    file = open("C:\\Users\\10291\\OneDrive\\dd.txt", 'w')
    file.write('')
    file.close()


a = 0
clear_txt()
while True:
    a = a + 1
    text = requests.get('http://txt.go.sohu.com/ip/soip').text
    ip = re.findall(r'\d+.\d+.\d+.\d+', text)
    ip = ip[0]
    sysTime = time.strftime('%H:%M:%S', time.localtime(time.time()))
    print(sysTime)
    print(ip)
    text_create('dd', "# " + sysTime + "\n    " + ip)
    print(a)
    time.sleep(600*3)
