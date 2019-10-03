'''
@Descripttion: 
@Author: daxiong
@Date: 2019-09-03 15:55:51
@LastEditors: daxiong
@LastEditTime: 2019-09-25 20:33:40
'''
s = input().strip().split()
s = [int(i) for i in s]

newArr = list() # 以类似插入排序的方式
newArr.append(s[0])

resNum = 0 # 能力值
maxNum = 0 # 最大的值
priorNum = s[0] # 前面一个数
sameNum = 0 # 相同的值
littleNum = 0 # 小于当前数的个数
biggerNum = 0 # 大于当前数的个数
lenList = 1 # 当前数组的总长
curIndex = 0

for num in s[1:]:
    if num == priorNum:
        resNum = resNum + littleNum - biggerNum
    elif num < priorNum:
        while curIndex >= 0 and newArr[curIndex] > num:
            curIndex -= 1
    else:
        
    priorNum = num
    lenList += 1
    if resNum > maxNum:
        maxNum = resNum
