'''
@Descripttion: 数轴游戏
@Author: daxiong
@Date: 2019-09-20 20:38:04
@LastEditors: daxiong
@LastEditTime: 2019-09-20 21:26:10
'''
n = int(input().strip())
arr = [int(x) for x in input().strip().split()]
arr.sort()

resNum = 0
for i in range(len(arr) - 1):
    for j in range(i + 1, len(arr)):
        if abs(arr[i]) *2 >= abs(arr[j]) or abs(arr[i]) <= abs(arr[j]) * 2:
            resNum += 1

print(resNum)