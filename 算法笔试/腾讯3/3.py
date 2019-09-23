'''
@Descripttion: 
@Author: daxiong
@Date: 2019-09-20 20:38:07
@LastEditors: daxiong
@LastEditTime: 2019-09-20 21:38:22
'''
s = input().strip().split()
n, k = int(s[0]), int(s[1])

arr = list()
for i in range(n):
    s = input().strip().split()
    a, b = int(s[0]), int(s[1])
    arr.append([a, b])

arr.sort(reverse = True)
resNum = 0
Kval = 0
minK = arr[k-1][0]
minVal = arr[0][1]
for i in range(k):
    Kval += arr[i][0]
    if arr[i][1] < minVal:
        minVal = arr[i][1]

resNum = minVal * Kval
for i in range(k, n):
    if (Kval - minK + arr[i][0]) * min(arr[i][1], minVal) > resNum:
        resNum = (Kval - minK + arr[i][0]) * min(arr[i][1], minVal)
print(resNum)
            