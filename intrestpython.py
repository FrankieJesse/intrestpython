# python 的基础数据类型只有六种类：
import random
def GetClassType(inputPara) :
    print("intpu para's value is %s" % str(inputPara))
    print("the input parameter's type is %s " % type(inputPara))

# 从个位开始，将一个数字的各个位置上的数值打印出来
def GetDigitalNum(num) :
    num = int(num)
    numString = str(num)
    for index in range(len(numString)) :
        # base = 10 ** index
        positionNum = num % 10
        print("the %d pos num = %d" %(index, positionNum))
        num /= 10

# 判断一个年份是否是闰年
def IsLeapYear(year) :
    yearInput = int(year)
    yearInput = random.randint(2000, 2020)
    print("input year is : %s" %str(year))
    if (yearInput % 400 == 0) or (yearInput % 4 == 0 and yearInput % 100 != 0) :
        print("%d is leap year" %yearInput)
    else :
        print("%d is not leap year" %yearInput)

# 1 + 2 + 3 + ... + 100
def SumNum(num) :
    index = int(num)
    sum = 0
    while index >= 0 :
        sum += index
        index -= 1
    print("1+2+3+...+%d = %d" %(int(num), sum))

# print triangle
def PrintTriangle() :
    loopNum = 8
    startNum = 1
    lineChar = 17
    while loopNum >= 0 :
        print("%s%s" %(" " *  int((lineChar - startNum) / 2), "*" * startNum))
        startNum += 2
        loopNum -= 1

# 寻找完全数，如果一个数，恰好是他的因子之和，则称之为完全数。
def FindPerfectNum(num) :
    list = [1]
    base = int(num) - 1
    # attention : [2, num)
    for index in range(2, num) :
        if int(num) % index == 0 :
            list.append(index)
            base -= index
    if base == 0 :
        print("the num %d is perfect num, and the subNum are :" %num)
        for loopCOunt in range(len(list)) :
            print("%d" %list[loopCOunt])
    else :
        print("the num %d is not perfect num" %num)

# intrest python main function
def IntrestPythonMain() :
    maxNum = 10
    for integerIndex in range(maxNum) :
        print()
        for nextNum in range(1, integerIndex + 1) :
            print("%2d * %2d = %2d" %(integerIndex, nextNum, integerIndex * nextNum), end = "  ")
        print("")

    # define some variables
    interger1, string1, string2 = 10, 'Frankie', 'Jesse'
    GetClassType(interger1)
    GetClassType(string1)
    GetClassType(string2)
    GetDigitalNum(12345)
    IsLeapYear(2012)
    SumNum(100)
    PrintTriangle()
    FindPerfectNum(6)
