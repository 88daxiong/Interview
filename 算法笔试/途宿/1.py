'''
@Descripttion: 寻找最大数
@Author: daxiong
@Date: 2019-09-06 20:31:58
@LastEditors: daxiong
@LastEditTime: 2019-09-06 20:41:30
'''
s = input().strip().split()
strL = [int(x) for x in s[0]]
m = int(s[1])
newLength = len(strL) - m
newNum = ''

while newLength != 0: # 一个一个的找到最大的数字
    maxNum = max(strL[: len(strL) - newLength + 1])
    newNum += str(maxNum)
    strL = strL[strL.index(maxNum) + 1: ]
    newLength -= 1

print(newNum)