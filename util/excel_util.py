#coding=utf-8

import xlrd
import os

class ExcelUtil:
    def __init__(self,excel_path=None,index=None):
        if excel_path == None:
            excel_path = os.path.join(os.getcwd()+'/data/testcase_data.xlsx')
        if index == None:
            index = 0
        print('Excel_path: ',excel_path)
        self.data = xlrd.open_workbook(excel_path)
        self.table = self.data.sheets()[index]
        self.rows = self.table.nrows

    def get_data(self):
        result = []
        for i in range(1,self.rows):
            col = self.table.row_values(i)
            result.append(col)
        print('result: ', result)
        return result



if __name__ == '__main__':
    # ex = ExcelUtil(None,1)
    ex = ExcelUtil()
    ex.get_data()
