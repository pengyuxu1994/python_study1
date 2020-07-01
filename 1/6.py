num=eval(input("请输入0-15"))

'''
if num<0 or num>15:
    print("输入错误")
else:
    if num>1 and num<9:
        print("num")
    elif num==10:
        print("A")
    elif num==11:
        print("B")
    elif num==12:
        print("C")
    elif num==13:
        print("D")
    elif num==14:
        print("E")
    else:
        print("F")
'''
if num<0 or num>15:
    print("error")
else:
    if num>0 and num<10:
        print(num)
    else:
        print(chr(ord("A")+num-10))