# coding = utf-8
__author__ = 'Aimee'

import requests
import os
import xlrd

filename = "测试资源 .xlsx"
file = os.path.join(os.getcwd(),filename)
'''一、打开文件'''
xl = xlrd.open_workbook(file)
'''二、获取sheet'''
# print(xl.sheet_names())  #获取所有的sheet
# print(xl.sheets())
# print(xl.sheet_by_name('目录')) #获取某一个sheet
# print(xl.sheet_by_name('加QQ群205089395获取'))
# print(xl.sheet_by_index(1))
# print(xl.nsheets) #多少个sheet

'''获取sheet内的汇总数据'''
table1 = xl.sheet_by_name('目录')
print(table1.name)
print(table1.nrows) #某一个sheet表中有多少行
print(table1.ncols) #某一个sheet表中有多少列

'''单元格批量读取'''
print(table1.row_values(1))


