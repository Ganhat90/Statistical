Si_So = int(input("Nhập số học sinh trong lớp: "))

Class_6A1 = []
for hs in range(Si_So):
    name = input("Nhập tên học sinh: ")
    Class_6A1.append(name)

print("Danh sách lớp 6A1: ",Class_6A1)
# 1. Thống kê xem có bao bạn có trùng tên, và trùng tên gì. VD: 2 An, 3 Anh, ...
countName = {}
for i in range(0, len(Class_6A1)):
  fullname = Class_6A1[i].split(" ")
  name = fullname[len(fullname)-1]
  if name in countName:
     countName[name] += 1
  else:
     countName[name] = 1
for LastName, value in countName.items():
  if value > 1:
    print(value, LastName)