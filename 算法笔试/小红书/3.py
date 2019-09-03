'''
@Descripttion: 
@Author: daxiong
@Date: 2019-09-03 20:49:46
@LastEditors: daxiong
@LastEditTime: 2019-09-03 20:56:27
'''
N = int(input().strip())
arr = list()
for i in range(N):
    s = input().strip().split()
    arr.append((int(s[0]), int(s[1])))

arr.sort(key=lambda x: (x[0], x[1]))
resNum = 1
print(arr)
a, b = arr[0][0], arr[0][1]
for i in range(1, N):
    if arr[i][0] >= a and arr[i][1] >= b:
        resNum += 1
        a = arr[i][0]
        b = arr[i][1]
    
print(resNum)