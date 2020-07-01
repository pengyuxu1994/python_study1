'''
linstr="陈萌,010-116321,M,19000101,北京市海淀区苏州街3号大恒科技大厦北座6层"
mylist = linstr.split(",")#字符串切割
print(mylist)#打印列表
print(mylist[2])#打印列表的第三个元素
'''
linstr = "456or123 # 15821 # ycb_wizard@163.net"
mylist = linstr.split(" # ")
print(mylist)
print(mylist[2])