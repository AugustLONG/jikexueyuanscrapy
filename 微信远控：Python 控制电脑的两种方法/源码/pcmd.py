import subprocess
import os
import time
# os.system('ping www.baidu.com')

# a = subprocess.Popen('dir', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
#
# b = a.stdout.readlines()
# for i in b:
#     print i

#运行这个程序之前记得按照视频把conf.txt改过来哦，否则会报错。
while True:
    f = open('conf.txt', 'r')
    content = f.read()
    os.system(content)
    time.sleep(5)