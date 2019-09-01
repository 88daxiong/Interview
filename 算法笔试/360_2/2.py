'''
@Descripttion: 散步
@Author: daxiong
@Date: 2019-08-31 17:42:47
@LastEditors: daxiong
@LastEditTime: 2019-08-31 17:52:43
'''

s = input().strip().split()
N = int(s[0])
M = int(s[1])
info = list()
for i in range(M):
    info.append(int(input().strip()))

num = set()

def dfs(d, idx, pos, n, fa):
    if idx >= len(d) and pos >= 0 and pos < n:
        num.add(pos)
        return
    if d[idx] <= pos:
        dfs(d, idx + 1, pos - d[idx], n, fa)
    
    if d[idx] <= n - 1- pos:
        dfs(d, idx + 1, pos + d[idx], n, fa)

resNum = 0
for i in range(N):
    dfs(info, 0, i, N, i)

print(num)
print(len(num))


