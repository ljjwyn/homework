import random
import time

import testName
import string
import pymysql



Prog_ID=["HNZIS","COMPFIN","HNZBI","AI"]
Prog_Name=["Information Systems","Computational Finance","Business Intelligence and Data Analytics","Artificial Intelligence"]
Comp_ID=["C8","C10","C18","C19","C21","C22","C25","C28","C29","C30"]
Comp_Name=["Newell","Caracas","Bell","Simon","Hobbit","Azkaban","Avatar","Dinar","Goldeneye","Barnaby"]
Location_ID=[1,2,3]
Item_ID=[15,17,19,21,23,25]
Vendor=["Best Buy","Dell","HP","Campus Store","Apple Store"]
Item_Manuf=["Dell","HP","Lenovo","Lenovo","HP","Dell"]
Item_Model=["Studio XPS","Pavilion Elite","ThinkStation","IdeaPad","Mini","Vostro"]
compTime=[]
list_HBH=list(range(100, 144))
list_NSH=list(range(203, 254))
num = list(range(1, 11))


def insert_into_student(id,firstName,lastName,Email,progId):
    conn = pymysql.connect(
        host='localhost',
        user='root',
        password='',
        db='studentloaninformation',
        port=3306
    )
    cur = conn.cursor()  # 获取操作游标，也就是开始操作
    sql = "INSERT INTO student (St_ID,St_LName,St_FName,Email,Prog_ID) VALUES (%s,%s,%s,%s,%s)"
    values =(id,firstName,lastName,Email,progId)
    cur.execute(sql,values)
    conn.commit()
    conn.close()


def insert_into_location(id,bldg,room):
    conn = pymysql.connect(
        host='localhost',
        user='root',
        password='',
        db='studentloaninformation',
        port=3306
    )
    cur = conn.cursor()  # 获取操作游标，也就是开始操作
    sql = "INSERT INTO location (Location_ID,Loc_Bldg,Loc_Room) VALUES (%s,%s,%s)"
    values =(id,bldg,room)
    cur.execute(sql,values)
    conn.commit()
    conn.close()


def insert_into_computer(Comp_ID,Comp_Name,Purchase_Date,Purchase_Price,Location_ID,Item_ID,Vendor):
    conn = pymysql.connect(
        host='localhost',
        user='root',
        password='',
        db='studentloaninformation',
        port=3306
    )
    cur = conn.cursor()  # 获取操作游标，也就是开始操作
    sql = "INSERT INTO computer (Comp_ID,Comp_Name,Purchase_Date,Purchase_Price,Location_ID,Item_ID,Vendor) VALUES (%s,%s,%s,%s,%s,%s,%s)"
    values =(Comp_ID,Comp_Name,Purchase_Date,Purchase_Price,Location_ID,Item_ID,Vendor)
    cur.execute(sql,values)
    conn.commit()
    conn.close()


def insert_into_loan(Loan_ID,St_ID,Comp_ID,Start_Date,Date_Returned):
    conn = pymysql.connect(
        host='localhost',
        user='root',
        password='',
        db='studentloaninformation',
        port=3306
    )
    cur = conn.cursor()  # 获取操作游标，也就是开始操作
    sql = "INSERT INTO loan (Loan_ID,St_ID,Comp_ID,Start_Date,Date_Returned) VALUES (%s,%s,%s,%s,%s)"
    values =(Loan_ID,St_ID,Comp_ID,Start_Date,Date_Returned)
    cur.execute(sql,values)
    conn.commit()
    conn.close()


def getFirstLastName(lowercase=False):
    size = len(testName.ALL_ENG_NAMES) - 1
    idx_name = random.randint(0, size)
    name = testName.ALL_ENG_NAMES[idx_name][1:]
    if lowercase:
        name = name.lower()
    return name


def getStudentId():
    digitmax=10
    digit = random.randint(1, int(digitmax))
    try:
        num.index(digit)
        num[num.index(digit)]=0
        flag=1
    except:
        flag=0
    return flag,digit


def getHBHLocRoom():
    digitmax=143
    digit = random.randint(100, int(digitmax))
    try:
        list_HBH.index(digit)
        list_HBH[list_HBH.index(digit)]=0
        flag=1
    except:
        flag=0
    return flag,digit


def getNSHLocRoom():
    digitmax=253
    digit = random.randint(203, int(digitmax))
    try:
        list_NSH.index(digit)
        list_NSH[list_NSH.index(digit)]=0
        flag=1
    except:
        flag=0
    return flag,digit


def getEmail():
    ran_str = ''.join(random.sample(string.ascii_letters, 6))
    ran_str=ran_str+"@ouc.edu.cn"
    return ran_str


def getProgId():
    size = len(Prog_ID) - 1
    idx_name = random.randint(0, size)
    name = Prog_ID[idx_name]
    return name

def getTime():
    a1 = (2018, 1, 1, 0, 0, 0, 0, 0, 0)  # 设置开始日期时间元组（1976-01-01 00：00：00）
    a2 = (2018, 9, 1, 23, 59, 59, 0, 0, 0)  # 设置结束日期时间元组（1990-12-31 23：59：59）
    start = time.mktime(a1)  # 生成开始时间戳
    end = time.mktime(a2)  # 生成结束时间戳
    t = random.randint(start, end)  # 在开始和结束时间戳中随机取出一个
    date_touple = time.localtime(t)  # 将时间戳生成时间元组
    date = time.strftime("%Y-%m-%d", date_touple)  # 将时间元组转成格式化字符串（1976-05-21）
    return t,date


def setTime(nowTime):
    a2 = (2019, 5, 1, 23, 59, 59, 0, 0, 0)  # 设置结束日期时间元组（1990-12-31 23：59：59）
    end = time.mktime(a2)  # 生成结束时间戳
    t = random.randint(nowTime, end)  # 在开始和结束时间戳中随机取出一个
    date_touple = time.localtime(t)  # 将时间戳生成时间元组
    date = time.strftime("%Y-%m-%d", date_touple)  # 将时间元组转成格式化字符串（1976-05-21）
    print(date)
    return date,t


def setStartTime(nowTime):
    end = nowTime+100000  # 生成结束时间戳
    t = random.randint(nowTime, end)  # 在开始和结束时间戳中随机取出一个
    date_touple = time.localtime(t)  # 将时间戳生成时间元组
    date = time.strftime("%Y-%m-%d", date_touple)  # 将时间元组转成格式化字符串（1976-05-21）
    print(date)
    return date,t


def insertStudents():
   for i in range(1001,1201):
        name=getFirstLastName()
        print(name)
        print(getFirstLastName())
        print(getEmail())
        print(getProgId())
        insert_into_student(i,getFirstLastName(),getFirstLastName(),getEmail(),getProgId())



def insertLocation():
    i = 0
    for j in range(1, 31):
        digit = random.randint(0, 1)
        if digit == 0:
            flags = 0
            while flags == 0:
                flags, id = getHBHLocRoom()
            insert_into_location(j, "HBH", id)
        else:
            flags = 0
            while flags == 0:
                flags, id = getNSHLocRoom()
            insert_into_location(j, "NSH", id)


def insertComputer():
    for i in range(1, 101):
        item = str(i)
        itemId = "C" + item
        nowTime, date = getTime()
        compTime.append(nowTime)
        print(nowTime, date)
        comName = getFirstLastName()
        print(comName)
        price = random.randint(1000,4000)
        loc_id = random.randint(1,31)
        size = len(Item_ID) - 1
        idx_name = random.randint(0, size)
        item = Item_ID[idx_name]
        print(price,loc_id,item)
        size = len(Vendor) - 1
        idx_name = random.randint(0, size)
        vendor = Vendor[idx_name]
        insert_into_computer(itemId,comName,date,price,loc_id,item,vendor)

#1555226728
def insertLoan():
    for i in range(1,300):
        student_id = random.randint(1001, 1201)
        comp_id = random.randint(1, 100)
        while compTime[comp_id - 1]==0:
            comp_id = random.randint(1, 100)
        item = str(comp_id)
        itemId = "C" + item
        nowTime = compTime[comp_id - 1]
        startDate, timeStep = setStartTime(nowTime)
        if timeStep >= 1555226728:
            returnDate = ""
            compTime[comp_id - 1] = 0
        else:
            returnDate, endTimeStep = setTime(timeStep)
            print(itemId, startDate, returnDate)
            compTime[comp_id - 1] = endTimeStep
        insert_into_loan(i, student_id, itemId, startDate, returnDate)


if __name__ == '__main__':
    insertStudents()
    insertLocation()
    insertComputer()
    insertLoan()
