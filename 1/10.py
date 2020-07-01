import time


'''
starttime=time.time()
lasttime=0
num=0
while num<300000000:
    num+=1
    lasttime+=num
print(lasttime)
endtime=time.time()
print(endtime-starttime)
'''
strttime=time.time()
lasttime=0
for i in range(300000000):
    lasttime+=i
print(lasttime)
endtime=time.time()
print(endtime-strttime)

