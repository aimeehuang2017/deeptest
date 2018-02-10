__author__ = 'Aimee'
import xlrd

class XLDatainof(object):
    def __init__(self,path = ''):
        self.xl =xlrd.open_workbook(path)

    def get_sheetinfo_by_name(self,name):
        self.sheet = self.xl.sheet_by_name(name)
        return self.get_sheet_info()

    def get_sheet_info(self):
        infolist = []
        for row in range (0,self.sheet.nrows):
            info = self.sheet.row_values(row)
            infolist.append(info)
        return infolist

if __name__ == "__main__":

    datainfo = XLDatainof(r'D:\20180101\ceshi\deeptest\第一期\广州-Aimee\interface\test_data\post_json_test_data.xlsx')
    alldata = datainfo.get_sheetinfo_by_name('AllData')
    print(alldata[1])
