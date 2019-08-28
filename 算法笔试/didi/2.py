'''
@Descripttion: 多源D点
@Author: daxiong
@Date: 2019-08-27 20:37:40
@LastEditors: daxiong
@LastEditTime: 2019-08-27 21:09:26
'''
# T = input().strip().split(' ')
# n, m, d = int(T[0]), int(T[1]), int(T[2])
# T = input().strip()
# limited = [int(x) for x in T.split(' ')]
# T = input().strip()
# temp = [int(x) for x in T.split(' ')]
n, m, d = 6, 2, 3
limited = [1, 2]
temp = [3, 4, 5, 6, 1]

res = list()
res.append(2)
while len(res) < n:
    x = res[-1]
    res.append(temp[x - 2])

for i in range(m):
    limited[i] = res.index(limited[i]) + 1

limited.sort()
if m == 1:
    print(min(2*d + 1, n))
if m >= 2:
    dis = limited[-1] - limited[0]
    if dis > 2 * d:
        print(0)
    else:
        print(min(2*d - dis + 1, n))

    

# 6 2 3
# 2 1
# 3 4 5 6 1