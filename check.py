import math

its = {
    1:"one", 2:"two", 3:"three", 4:"four", 5:"five",
    6:"six", 7:"seven", 8:"eight", 9:"nine"
}
itt = {
    1:"teen", 2:"twenty", 3:"thirty", 4:"fourty", 5:"fifty",
    6:"sixty", 7:"seventy", 8:"eighty", 9:"ninety"
}
teens = {
    1:"eleven", 2:"twelve", 3:"thirteen", 4:"fourteen", 5:"fifteen",
    6:"sixteen", 7:"seventeen", 8:"eighteen", 9:"nineteen"
}

def br(num):
    decimals = 100.0
    multiplied = num * decimals
    floored = math.floor(multiplied)
    remainder = multiplied - floored
    if remainder >= .5:
        floored += 1
    rounded = str(floored / decimals)
    while len(rounded) - rounded.index('.') <= 2:
        rounded += '0'
    return float(rounded)
    
def calc(num):
    while num > 0 and num < 1000:
        # if num >= 10000:
        #     print(its.get(int(num/10000)),end=" ")
        #     num -= int(num/100) * 10000
        # if num >= 1000:
        #     print(its.get(int(num/1000)),end=" thousand ")
        #     num -= int(num/1000) * 1000
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
    dec = int(br(num % 1)*100)
    num = math.floor(num)
    secs = list()
    num = list(str(num))
    num.reverse()
    if len(num) % 3 == 2:
        num.append(0)
    if len(num) % 3 == 1:
        num.append(0)
        num.append(0)
    run = True
    while run:
        temp = ""
        for i in range(3):
            temp += str(num.pop(i))
        secs.append(int(temp))
    for sec in secs:
        calc(sec) 
    if dec != 0:
        print("and", dec, "/ 100", end = " ")
    
user_in = None
while user_in != 0:
    user_in = float(input("Please enter a number between 0 and 1 million inclusive: "))
    write(user_in)
    print()