import math

its = { 1:"one", 2:"two", 3:"three", 4:"four", 5:"five", 6:"six", 7:"seven", 8:"eight", 9:"nine" }
itt = { 2:"twenty", 3:"thirty", 4:"fourty", 5:"fifty", 6:"sixty", 7:"seventy", 8:"eighty", 9:"ninety" }
teens = { 1:"eleven", 2:"twelve", 3:"thirteen", 4:"fourteen", 5:"fifteen", 6:"sixteen", 7:"seventeen", 8:"eighteen", 9:"nineteen" }
mil = { 0:"", 1:"thousand ", 2:"million ", 3:"billion ", 4:"trillion ", 5:"quadrillion ", 6:"quintillion ", 7:"sextillion ", 8:"heptillion ", 9:"octillion ", 10:"nonillion ", 11:"decillion ", 12:"undecillion ", 13:"duodecillion ", 14:"tredecillion ", 15:"quattuordecillion ", 16:"quindecillion ", 17:"sexdecillion ", 18:"septen-decillion ", 19:"octodecillion ", 20:"novemdecillion ", 21:"vigintillion " }

def calc(num):
    while num > 0 and num < 1000:
        if num >= 100:
            print(its.get(int(num/100)),end=" hundered ")
            num -= int(num/100) * 100
        elif num >= 20:
            print(itt.get(int(num/10)),end=" ")
            num -= int(num/10) * 10
        elif num > 10:
            print(teens.get(int(num%10)),end=" ")
            num -= 10+int(num%10)
        elif num == 10:
            print("ten",end=" ")
            num -= 10
        elif num >= 1:
            print(its.get(int(num)),end=" ")
            num -= int(num)

def write(num):
    if "." in num:
        num, dec = (str(val) for val in num.split("."))
        dec = int(dec[0:2])
    else:
        dec = 0
    secs = list()
    num = list(num)
    if len(num) % 3 == 2:
        num.insert(0,"0")
    if len(num) % 3 == 1:
        num.insert(0,"0")
        num.insert(0,"0")
    for i in range(int(len(num)/3)):
        l = num[i*3:(i*3)+3]
        temp = ""
        for val in l:
            temp += val
        secs.append(int(temp))
    count = len(secs)-1
    for sec in secs:
        calc(sec)
        if sec != 0:
            print(mil.get(count),end="")
        count -= 1
    if dec != 0:
        print("and", dec, "/ 100", end = " ")
    
user_in = None
while user_in != 0:
    user_in = input("Please enter a number between 0 and 100 vigintillion inclusive: ")
    write(user_in)
    print("\n")