# _*_ coding:utf-8 _*_
# @Time    :2019/5/24 11:12
# @Author  :xiuhong.guo
# @Email   :892336120@qq.com
# @File    :HomeWork.py

# 作业：写一个类，类里面有2个方法，一个读数据，一个写数据，读数据可以读取整个Excel里面的所有数据，每一行数据都放在一个列表里，
# 所有的数据放在一个大列表里，写数据可以在Excel里面指定的单元格里面写入指定的值
# from openpyxl import load_workbook
# class OpenpyxlLoad:
#     def __init__(self,ExcelName,SheetName):
#         self.ExcelName=ExcelName
#         self.SheetName=SheetName
#     def ReadData(self):
#         wb = load_workbook(self.ExcelName)
#         sheet=wb[self.SheetName]
#         B_list=[]
#         for i in range(1,sheet.max_row + 1): # 控制行 5
#             S_list=[]
#             for j in range(1, sheet.max_column + 1): # 控制列 4
#                 S_list.append(sheet.cell(i,j).value)
#             B_list.append (S_list)
#         wb.close()
#         return B_list
#     def WriteData(self,hang,lie,date):
#         wb = load_workbook(self.ExcelName)
#         sheet=wb[self.SheetName]
#         sheet.cell(hang,lie,date)
#         wb.save(self.ExcelName)
#         wb.close()
#
# if __name__ == '__main__':
#     OpenpyxlLoad_class=OpenpyxlLoad('python_1bb.xlsx','Sheet')
#     OpenpyxlLoad_class.WriteData(1,2,'345')
#     B_list=OpenpyxlLoad_class.ReadData()
#     print(B_list)






