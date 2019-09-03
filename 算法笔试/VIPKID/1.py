'''
@Descripttion: 二进制表示1的个数
@Author: daxiong
@Date: 2019-09-03 15:55:46
@LastEditors: daxiong
@LastEditTime: 2019-09-03 16:41:56
'''
a = int(input().strip())
resNum = 0
while a != 0:
    a &= a - 1
    resNum += 1

print(resNum)