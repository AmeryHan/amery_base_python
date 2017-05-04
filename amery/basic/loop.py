# -*- coding: UTF-8 -*-
'''
count = 0
while (count < 9):
    print 'The count is:', count
    count = count + 1

print "Good bye!"



sequence = [12, 34, 34, 23, 45, 76, 89]
for i, j in enumerate(sequence):
   print i,j

'''
prime = []
for num in range(2, 100):
    for i in range(2, num):
        if num % i == 0:
            break;
        else:
            prime.append(num)
print prime


prime = []
for num in range(2, 100):
    for i in range(2, num):
        if num % i == 0:
            break;
    else:
        prime.append(num)
print prime

i = 2
while(i < 100) :
    j = 2
    while (j <= (i / j)) :
        if not (i % j) : break
        j = j + 1
    if (j > i / j) : print i, " 是素数"
    i = i + 1

print "Godd bye!"


for letter in "Python" :
    if letter == 'h' :
        break
    print 'current letter : ', letter

var = 10
while var > 0:
    print 'current :', var
    var = var - 1
    if var == 5 :
        break

print 'Goodbye'


for letter in 'Python':
   if letter == 'h':
      pass
      print '这是 pass 块'
   print '当前字母 :', letter

print "Good bye!"

var1 = 'Hello World!'
var2 = "Python Runoob"

print "var1[0]: ", var1[0]
print "var2[1:5]: ", var2[1:5]

