import xlrd,datetime,os
from get_config import config
from xlrd import xldate_as_tuple


# data = xlrd.open_workbook("F:/jiaoyan/test_data/data.xlsx")
# print(data)
# data.sheet_names()  # 获取所有表名称
# table = data.sheet_by_index(0)    # 获取表名称的行列内容
# print(table)
# name = table.name   # 名称
# print(name)
# rownum = table.nrows    # 行数
# print(rownum)
# colnum = table.ncols    # 列数
# print(colnum)
# # 读取表格的值
# print(int(table.cell(1,1).value))
# print(int(table.cell_value(2, 1)))
# print(table.row(2)[0])
#
# print(table.row(0)) # 获取第一行数据

"""
表格数据类型：
0 empty,
1 string,
2 number,
3 date,
4 boolean,
5 error
"""

class ExcelData():
    def __init__(self,file,sheetname):
        data_path = config().get_excel("excel_data")
        file_path = os.path.join(data_path,file)
        data = xlrd.open_workbook(file_path)
        self.sheetname = sheetname
        self.table = data.sheet_by_name(self.sheetname)
        self.keys = self.table.row_values(1)
        self.rowNum = self.table.nrows
        self.colNum = self.table.ncols


    def read_excel(self):
        datas = []
        for i in range(2,self.rowNum):
            sheet_data = {}
            for j in range(0,self.colNum):
                c_type = self.table.cell(i,j).ctype     # 2
                c_value = self.table.cell(i,j).value
                if c_type == 2 and c_type % 1 == 0:
                    c_value = int(c_value)
                    c_value = str(c_value)
                elif c_type == 3:
                    data = datetime.datetime(*xldate_as_tuple(c_value, 0))
                    c_value = data.strftime('%Y-%m-%d %H:%M:%S')
                elif c_type == 4:
                    c_value = True if c_value == 1 else False
                sheet_data[self.keys[j]] = c_value
            datas.append(sheet_data)

        return datas


    def get_excel_value(self,key):
        datas = self.read_excel()
        for data in datas[0:len(datas):]:
            return data[key]


    def get_col_value(self,data,key):
        for i in data[0:len(data)]:
            print(i[key])
            return i[key]






if __name__ == '__main__':
    A = ExcelData("test_case.xlsx","Sheet1")
    data = A.read_excel()
    print(type(data))
    # for i in data[0:len(data)]:
    #     print(i["param"])
    # print(type(data))
    # for x in range(len(data)):
    #      value = data[x]
    #      print(type(value))
    #      i = value["param"]
    #      print(i)
    data1 = A.get_excel_value("param")
    print(data1)


