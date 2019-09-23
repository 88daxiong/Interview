'''
@Descripttion: 柠檬的选择
@Author: daxiong
@Date: 2019-09-20 20:38:01
@LastEditors: daxiong
@LastEditTime: 2019-09-20 20:53:07
'''
s = input().strip().split()
n, m = int(s[0]), int(s[1])

lemonA = [int(x) for x in input().strip().split()]
lemonB = [int(x) for x in input().strip().split()]
lemonA.sort()
lemonB.sort()

a, b, c, d = lemonA[0],lemonA[1], lemonA[-2], lemonA[-1] 
m, n = lemonB[0], lemonB[-1]
maxAB = max(a*m, a*n, d*m, d*n)
if a*m == maxAB or a*n == maxAB: # 这种情况去掉a
    print(max(b*m, b*n, d*m, d*n))
else: #这种情况去掉a
    print(max(a*m, a*n, c*m, c*n))
