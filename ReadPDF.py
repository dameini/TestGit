#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 读取pdf文件
import PyPDF2

pdfFile = open('test.pdf', 'rb')

pdfReader = PyPDF2.PdfFileReader(pdfFile)

print(pdfReader.numPages)

page = pdfReader.getPage(165)

print(page.extractText())

pdfFile.close()
