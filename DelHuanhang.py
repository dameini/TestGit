#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# __author__ = "10291"
# 删除剪贴板文本中的换行符

import pyperclip
import time

a = 1
tt = pyperclip.paste()
print(pyperclip.paste())

copyBuff = ''
while True:
    time.sleep(2)
    CopiedText = pyperclip.paste()
    if copyBuff != CopiedText:
        copyBuff = CopiedText
        normalizedText = copyBuff.replace('\r\n', '')  # 将字符串中换行符删除
        pyperclip.copy(normalizedText)
        print(normalizedText)
    else:
        print('NoCopyText')
