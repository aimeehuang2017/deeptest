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

'''三、获取sheet内的汇总数据'''
table1 = xl.sheet_by_name('目录')
# print(table1.name)
# print(table1.nrows) #某一个sheet表中有多少行
# print(table1.ncols) #某一个sheet表中有多少列

'''四、单元格批量读取'''
# print(table1.row_values(1))  #合并单元格，首行显示值，其他为空  获取某一行的数值
# print(table1.row_values(1,0,2))
# print(table1.row_slice(1,0,2))
# print(table1.row_types(1,0,2))

# print(table1.row(1))  #某一行的类型加值

'''五、特定单元格读取'''
#取值
# print(table1.cell(1,2).value)  #读取某一个单元格值
# print(table1.cell_value(1,2))
# print(table1.row(1)[2].value)

#取类型
# print(table1.cell(1,2))
# print(table1.cell(1,2).ctype)
# print(table1.cell(1,2).ctype)
# print(table1.row(1)[2].ctype)
# print(table1.col(1)[2].ctype)

'''六、常用技巧（0,0）转化成A1'''

# print(xlrd.cellname(1,2))
# print(xlrd.cellnameabs(1,2))
# print(xlrd.colname(30))

'''七、获取表格内不同类型的name'''
print(table1.cell_value(1,0))
print(table1.cell(1,0).ctype)
print(table1.cell_type(1,0)) # 1字符串
print(table1.cell_value(0,1))
print(table1.cell_type(0,1))  #0空






