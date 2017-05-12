#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 文件名：test.py

if True:
    print "Answer"
    print "True"
else:
    print "Answer"
    # 没有严格缩进，在执行时会报错
    print "False"

item_one = 1
item_two = 2
item_three = 3
total = item_one + \
        item_two + \
        item_three

print total

days = ['Monday', 'Tuesday', 'Wednesday',
        'Thursday', 'Friday']

word = 'word'
sentence = "这是一个句子。"
paragraph = """这是一个段落。
包含了多个语句"""

# 第一个注释
print "Hello, Python!";  # 第二个注释

'''
这是多行注释，使用单引号。
这是多行注释，使用单引号。
这是多行注释，使用单引号。
'''

"""
这是多行注释，使用双引号。
这是多行注释，使用双引号。
这是多行注释，使用双引号。
"""

import sys; x = 'runoob'; sys.stdout.write(x + '\n')

#raw_input("\n\nPress the enter key to exit.")

x="a"
y="b"
# 换行输出
print x
print y

print '---------'
# 不换行输出
print x,
print y,

'''
if expression :
   suite
elif expression :
   suite
else :
   suite
'''

a, b, c = 1, 2, "john"

str = 'Hello World!'

print str  # 输出完整字符串
print str[0]  # 输出字符串中的第一个字符
print str[2:5]  # 输出字符串中第三个至第五个之间的字符串
print str[2:]  # 输出从第三个字符开始的字符串
print str * 2  # 输出字符串两次
print str + "TEST"  # 输出连接的字符串

list = ['runoob', 786, 2.23, 'john', 70.2]
tinylist = [123, 'john']

print list  # 输出完整列表
print list[0]  # 输出列表的第一个元素
print list[1:3]  # 输出第二个至第三个的元素
print list[2:]  # 输出从第三个开始至列表末尾的所有元素
print tinylist * 2  # 输出列表两次
print list + tinylist  # 打印组合的列表

tuple = ('runoob', 786, 2.23, 'john', 70.2)
tinytuple = (123, 'john')

#以下是元组无效的，因为元组是不允许更新的。而列表是允许更新的：
print tuple  # 输出完整元组
print tuple[0]  # 输出元组的第一个元素
print tuple[1:3]  # 输出第二个至第三个的元素
print tuple[2:]  # 输出从第三个开始至列表末尾的所有元素
print tinytuple * 2  # 输出元组两次
print tuple + tinytuple  # 打印组合的元组

dict = {}
dict['one'] = "This is one"
dict[2] = "This is two"

tinydict = {'name': 'john', 'code': 6734, 'dept': 'sales'}

print dict['one']  # 输出键为'one' 的值
print dict[2]  # 输出键为 2 的值
print tinydict  # 输出完整的字典
print tinydict.keys()  # 输出所有键
print tinydict.values()  # 输出所有值

a = 21
b = 10
c = 0

c = a + b
print "1 - c 的值为：", c

c += a
print "2 - c 的值为：", c

c *= a
print "3 - c 的值为：", c

c /= a
print "4 - c 的值为：", c

c = 2
c %= a
print "5 - c 的值为：", c

c **= a
print "6 - c 的值为：", c

c //= a
print "7 - c 的值为：", c


# 可写函数说明
def printinfo(arg1, *vartuple):
    "打印任何传入的参数"
    print "输出: "
    print arg1
    for var in vartuple:
        print var
    return;


# 调用printinfo 函数
printinfo(10);
printinfo(70, 60, 50);

sum = lambda arg1, arg2: arg1 + arg2

print "sum = ", sum(10, 20)

total = 0;  # 这是一个全局变量


# 可写函数说明
def sum(arg1, arg2):
    # 返回2个参数的和."
    total = arg1 + arg2;  # total在这里是局部变量.
    print "函数内是局部变量 : ", total
    return total;


# 调用sum函数
sum(10, 20);
print "函数外是全局变量 : ", total

a, b, c, d = 20, 5.5, True, 4+3j
print(type(a), type(b), type(c), type(d))
