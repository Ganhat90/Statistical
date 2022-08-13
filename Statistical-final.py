def input_choice(msg,ChoiceList):
    while True:
        try:
            string = input(msg)
            if string not in ChoiceList:
                print("Không hợp lệ chỉ chấp nhận: ",ChoiceList)
                continue
        except:
            print("Không hợp lệ")
            continue
        else:
            return string

def input_str(msg,NameList):
    while True:
        try:
            string = input(msg)
            if string in NameList:
                print("Không hợp lệ vì có kí tự trong: ",NameList)
                continue
        except:
            print("Không hợp lệ")
            continue
        else:
            return string

Si_So = int(input("Nhập số học sinh trong lớp: "))

Class_6A1 = []

choiceList = ['X','x','']
nameList = ['']

for hs in range(Si_So):
  stt = hs + 1

  print('\n\t ---- Học sinh ',stt,' ----')

  item = {"STT": stt}

  item["Họ và tên"] = input_str("Nhập tên học sinh: ",nameList)

  item["Bóng đá"] = input_choice("Bạn có đăng ký (x) bóng đá: ",choiceList)

  item["Bóng rổ"] = input_choice("Bạn có đăng ký (x) bóng rổ: ",choiceList)

  item["Võ"] = input_choice("Bạn có đăng ký (x) võ: ",choiceList)

  item["Cầu lông"] = input_choice("Bạn có đăng ký (x) cầu lông: ",choiceList)

  item["Yoga"] = input_choice("Bạn có đăng ký (x) yoga: ",choiceList)

  item["Nhịp điệu"] = input_choice("Bạn có đăng ký (x) nhịp điệu: ",choiceList)

  item["Dance sport"] = input_choice("Bạn có đăng ký (x) dance sport: ",choiceList)

  item["Sáo + NCDT"] = input_choice("Bạn có đăng ký (x) sáo + NCDT: ",choiceList)

  item["Organ"] = input_choice("Bạn có đăng ký (x) organ: ",choiceList)
  
  item["Ghita"] = input_choice("Bạn có đăng ký (x) ghita: ",choiceList)
  
  item["Mỹ thuật"] = input_choice("Bạn có đăng ký (x) mỹ thuật: ",choiceList)

  item["Thanh nhạc"] = input_choice("Bạn có đăng ký (x) thanh nhạc: ",choiceList)

  Class_6A1.append(item)
# 1. Thống kê xem có bao bạn có trùng tên, và trùng tên gì. VD: 2 An, 3 Anh, ...
print('---Thống kê xem có bao bạn có trùng tên, và trùng tên gì. VD: 2 An, 3 Anh, ...---')
countName={}
for i in range(0,len(Class_6A1)):  
  fullname = Class_6A1[i]["Họ và tên"].split(" ")
  name = fullname[len(fullname)-1]
  if name in countName:
    countName[name]+=1
  else:
    countName[name]=1

for LastName,value in countName.items():
 if value>1:
   print(value,LastName)
# 2. Thống kê xem có bao nhiêu bạn đăng ký từng môn? 
print("---Thống kê xem có bao nhiêu bạn đăng ký từng môn?---")
register = {}

keys = list(Class_6A1[0].keys())

for i in range(3, len(keys)):
  register[keys[i]] = 0

for i in range(0, len(Class_6A1)):   
    for j in range(3, len(keys)):     
        choice = Class_6A1[i][keys[j]].lower()
        if choice == 'x':
          register[keys[j]] += 1
          
for key, value in register.items():
  print(key, ':', value)

# 3. Thống kê xem có bao nhiêu bạn cùng đăng ký Bóng rổ & Mỹ thuật
print('---Thống kê xem có bao nhiêu bạn cùng đăng ký Bóng rổ & Mỹ thuật---')
count = 0

for i in range(0, len(Class_6A1)):      
  choice1 = Class_6A1[i][keys[4]].lower()
  choice2 = Class_6A1[i][keys[13]].lower()
  if choice1 == 'x' and choice2 == 'x':
     count += 1

print(count)
