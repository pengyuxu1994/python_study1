import win32process #进程模块
import win32con#xitogdingyi
import win32api
import ctypes
import win32gui

PROCESS_ALL_ACCESS=(0X000F0000|0X00100000|0XFFF)
window=win32api.Findwindow("MainWindow","植物大战僵尸中文版")