# -*- coding: utf-8 -*-

import xlrd
import requests

class APiTool:

    def xlsee(self, xlsFile):
        sheetlist = []  # 用来保存表格所有数据
        rqapi = xlrd.open_workbook(xlsFile)   #打开文件
        sheet_name = rqapi.sheet_names()[0]  # 获取第一个sheet名称
        sheet = rqapi.sheet_by_name(sheet_name)  # 获取第一个sheet对象
        nrow = sheet.nrows   # 获取行总数
        for i in range(1,nrow):
            sheetlist.append(sheet.row_values(i))
        return sheetlist

    # def request(self, rqtype, rqurl, paramete, headers):
    #     self.rqurl = rqurl  # API地址
    #     self.rqtype = rqtype  # 请求类型get or post
    #     self.paramete = paramete  # 请求参数
    #     self.headers = headers  # 请求头
    #
    #     if rqtype == "get":
    #         apiresult = requests.get(url=rqurl, params=paramete, headers=headers)  # 发送请求
    #         return apiresult
    #     if rqtype == "post":
    #         apiresult = requests.post(url=rqurl, data=paramete, headers=headers)
    #         return apiresult
    #     else:
    #         print("请求参数错误，请求类型只支持get+post，请求地址支持string，参数支持dict")
    #


if __name__ == "__main__":
        apitest = APiTool()
        xlsFile = r"E:\apicase.xls"  # 文件路径
        sheetlist = apitest.xlsee(xlsFile)
        print sheetlist[0]
        # # print(type(sheetlist1[0][0]))
        # a= {'b':[1,2,5,8],'c':3,'d':2,'f':[1,2,3],'g':[1,2,3,[2,'2',2]],'h':'5'}
        # b= {'b':[1,2,'3'],'c':2,'e':'4','f':[1,2,3,5],'g':[1,2,3,[1,2]],'h':[1,2]}
        # apitest.Assert(a,b)




