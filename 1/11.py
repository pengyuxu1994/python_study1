import win32con
import win32gui
import time
import math
QQ=win32gui.FindWindow("TXGuiFoundation","QQ")
se=0.0
while True:
    se = 0.0
    while se-2*3.1415926535<0.000001:
        for i in range(100,10,-1):
            se+=0.1
            newx=int(400+(400+i)*math.cos(se))
            newy=int(400+(400+i)*math.sin(se))
            win32gui.SetWindowPos(QQ,win32con.HWND_TOPMOST,newx,newy,300,300,win32con.SWP_SHOWWINDOW)
    print(se)
