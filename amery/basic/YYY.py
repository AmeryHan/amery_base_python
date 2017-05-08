# -*- coding: UTF-8 -*-


# 导入模块
import support

# 现在可以调用模块里包含的函数了
support.print_func("Runoob")

import re
print(re.match('www', 'www.runoob.com').span())  # 在起始位置匹配
print(re.match('com', 'www.runoob.com'))         # 不在起始位置匹配

line = "Cats are smarter than dogs"

matchObj = re.match(r'(.*) are (.*?) .*', line, re.M | re.I)

if matchObj:
    print "matchObj.group() : ", matchObj.group()
    print "matchObj.group(1) : ", matchObj.group(1)
    print "matchObj.group(2) : ", matchObj.group(2)
else:
    print "No match!!"


print (re.search('www', 'www.runoob.com').span())
print (re.search('com', 'www.runoob.com').span())

try:
    fh = open("testfile", "w")
    fh.write("这是一个测试文件，用于测试异常!!")
except IOError:
    print "Error: 没有找到文件或读取文件失败"
else:
    print "内容写入文件成功"
    fh.close()


def temp_convert(var) :
    try:
        return int(var)
    except ValueError, Argument :
        print "no number\n", Argument

temp_convert("xyz")

#import MySQLdb

import thread
import time


# 为线程定义一个函数
def print_time(threadName, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print "%s: %s" % (threadName, time.ctime(time.time()))


# 创建两个线程
try:
    thread.start_new_thread(print_time, ("Thread-1", 2,))
    thread.start_new_thread(print_time, ("Thread-2", 4,))
except:
    print "Error: unable to start thread"

while 1:
    pass