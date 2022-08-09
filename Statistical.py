import xlrd
import numpy as np

workbook = xlrd.open_workbook("E:\\Python\\Exercise\\Other\\6A1.xlsx")
worksheet = workbook.sheet_by_index(0)

Names = []

for i in range(4, worksheet.nrows):
  name = worksheet.cell_value(i, 1).split(" ")
  if name[len(name)-1] != '':
    Names.append(name[len(name)-1])

# 1. Thống kê xem có bao bạn có trùng tên, và trùng tên gì. VD: 2 An, 3 Anh, ...
print("****Danh sách thống kê các bạn trùng tên****")
NamesUnique = np.unique(Names)
for i in range(0,len(NamesUnique)):
    name = NamesUnique[i]
    count = Names.count(name)
    if count != 1:
        print(str(count) + " " + name)

# 2. Thống kê xem có bao nhiêu bạn đăng ký từng môn? VD: Bóng rổ 19, Bóng đá 6, ...
print("****Danh sách thống kê số lượng học sinh đăng ký từng môn học****")
register = {}

for i in range(3, worksheet.ncols):
      register[worksheet.cell_value(3, i)] = 0

for i in range(4, worksheet.nrows):   
    for j in range(3, worksheet.ncols):     
        choice = worksheet.cell_value(i, j).lower()
        if choice == 'x':
          register[worksheet.cell_value(3, j)] += 1
          
for key, value in register.items():
    print(key, ':', value)

# 3. Thống kê xem có bao nhiêu bạn cùng đăng ký Bóng rổ & Mỹ thuật
print("****Danh sách thống kê xem có bao nhiêu bạn cùng đăng ký Bóng rổ & Mỹ thuật****")
count = 0

for i in range(4, worksheet.nrows):    
  choice1 = worksheet.cell_value(i, 4).lower()
  choice2 = worksheet.cell_value(i, 13).lower()
  if choice1 == 'x' and choice2 == 'x':
     count += 1
print(count)
