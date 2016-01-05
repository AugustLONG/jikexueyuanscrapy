#-*-coding:utf8-*-
import time
import win32api

win32api.Beep(8000,3000)


win32api.ShellExecute(0, 'open', r'F:\music\The Script\Science & Faith\09 Walk Away.wav', '', '', 1)


while True:
    f = open('conf.txt', 'r')
    content = f.read().split('#')
    if content[0] != '0':
        win32api.MessageBox(0, content[1], content[2])
    time.sleep(5)