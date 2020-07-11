#To save data in an excel

from pyexcel_xls import save_data
data = {"sheet1":[['sno','name','address'],[1,'abc','india']]}
save_data("demo.xls",data)

#To read the data from an excel

from pyexcel_xls import read_data
data = read_data("demo.xls")
print(data)

#Working with xlsxwriter

import xlsxwriter
workbook = xlsxwriter.Workbook('demo.xls')
worksheet = workbook.add_worksheet()
worksheet.write("A1",'test data')
worksheet.close()
