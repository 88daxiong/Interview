'''
@Description: In User Settings Edit
@Author: daxiong
@Date: 2019-08-15 18:44:38
@LastEditTime: 2019-08-16 10:52:18
@LastEditors: daxiong
'''


avg = input().strip().split()
N, M = int(avg[0]), int(avg[1])
arr = [[0]*M for i in range(N)]

for i in range(N):
    line = input().strip().split()
    for j in range(M):
        arr[i][j] = int(line[j])

area = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] != 0:
            area += arr[i][j] * 6 - (arr[i][j] - 1) * 2
        if i > 0 and arr[i-1][j] != 0:
            area -= min(arr[i-1][j], arr[i][j]) * 2
        if j > 0 and arr[i][j-1] != 0:
            area -= min(arr[i][j-1], arr[i][j]) * 2

print(area)


# 分为3个部分
# 1. 判断每一个点上的高度，然后如果大于1，则覆盖的面积为高度减1然后乘以2
# 2. 横列减去重叠的
# 3. 纵列减去重叠的
