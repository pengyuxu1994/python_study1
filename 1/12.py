import win32con
import win32gui

QQ=win32gui.FindWindow("TXGuiFoundation","QQ")
while True:
    for size in range(0,800,10):
        win32gui.SetWindowPos(QQ,win32con.HWND_TOPMOST,size,0,500,500,win32con.SWP_SHOWWINDOW)
    for size in range(0,600,10):
        win32gui.SetWindowPos(QQ,win32con.HWND_TOPMOST,800,size,500,500,win32con.SWP_SHOWWINDOW)
    for size in range(800,0,-10):
        win32gui.SetWindowPos(QQ,win32con.HWND_TOPMOST,size,600,500,500,win32con.SWP_SHOWWINDOW)
    for size in range(600,0,-10):
        win32gui.SetWindowPos(QQ,win32con.HWND_TOPMOST,0,size,500,500,win32con.SWP_SHOWWINDOW)
