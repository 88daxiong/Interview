'''
@Descripttion: 
@Author: daxiong
@Date: 2019-09-03 18:55:33
@LastEditors: daxiong
@LastEditTime: 2019-09-03 20:45:02
'''
strL = input().strip()

stack = list() # 存放（）里面的东西的
curStr = '' # 这个存放最终输出的东西
tag = 0
for c in strL:
    if c == '<':
        if curStr != '' and tag == 0:
            curStr = curStr[:-1]
    elif c == '(': # 第一个'('
        tag += 1
    elif c == ')':
        tag -= 1
    else:
        if tag == 0:
            curStr += c 

print(curStr)
