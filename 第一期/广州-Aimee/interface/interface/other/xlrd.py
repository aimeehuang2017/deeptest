# coding = utf-8
__author__ = 'Aimee'

import xlrd
import requests
import os

filename = "测试资源.xlsx"
file = os.path.join(os.getcwd(), filename)

xl = xlrd.open_workbook(file)
print(xl.sheet_names())
