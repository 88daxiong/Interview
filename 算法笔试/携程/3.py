'''
@Descripttion: 旅游路线设计
@Author: daxiong
@Date: 2019-09-04 20:16:30
@LastEditors: daxiong
@LastEditTime: 2019-09-04 20:51:54
'''

N = int(input().strip()) # 顶点数
M = int(input().strip()) # 通道数

inf = 100000000
dis = list()
minds = list()

for i in range(N + 1):
    dis.append([inf for x in range(N + 1)])
    minds.append([0 for x in range(N + 1)])
            
for i in range(M):
    s = input().strip().split()
    a, b, t = int(s[0]), int(s[1]), int(s[2])
    if dis[a][b] > t:
        dis[a][b] = t
        dis[b][a] = t

for i in range(1, N + 1):
    for j in range(1, N + 1):
        minds[i][j] = dis[i][j]

ansids = inf
anscnt = 0

for k in range(1, N + 1):
    for i in range(1, k):
        for j in range(i + 1, k):
            if ansids > dis[i][k] + dis[j][k] + minds[i][j]:
                ansids = dis[i][k] + dis[j][k] + minds[i][j]
                ansids = dis[i][k] + dis[j][k] + minds[i][j]
            elif ansids == dis[i][k] + dis[j][k] + minds[i][j]:
                anscnt += dis[i][k] + dis[j][k] + minds[i][j]
    
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            minds[i][j] = min(minds[i][j], minds[i][k] + minds[j][k])

if anscnt == 0:
    print(-1)
else:
    print(anscnt)
