'''
@Descripttion: 电信诈骗
@Author: daxiong
@Date: 2019-09-06 15:47:57
@LastEditors: daxiong
@LastEditTime: 2019-09-06 17:55:26
'''
s = input().strip().split()
K, N, M = int(s[0]), int(s[1]), int(s[2])

callMatrix = list()
for i in range(N):
    callMatrix.append([0 for x in range(N)]) # 初始化打电话的双方

for i in range(M):
    s = input().strip().split()
    caller, receiver, duration = int(s[0]), int(s[1]), int(s[2])
    callMatrix[caller - 1][receiver - 1] += duration

suspectList = list()

for i in range(N):
    numOfcall = 0 # 打出的电话
    numOfRecall = 0 # 打回的电话
    for j in range(N):
        if callMatrix[i][j] > 0 and callMatrix[i][j] <= 5:
            numOfcall += 1
            if callMatrix[j][i] > 0:
                numOfRecall += 1
    if numOfcall > K and (float(numOfRecall) / numOfcall) <= 0.2:
            suspectList.append(i + 1)

if len(suspectList) == 0:
    print("None")
    
associates = [] # 存放对
visited = [False for i in range(N)]
for i in range(len(suspectList)):
    for j in range(i + 1, len(suspectList)):
        a = suspectList[i] - 1
        b = suspectList[j] - 1
        if callMatrix[a][b] > 0 and callMatrix[b][a] > 0:
            tag = False
            for i in range(len(associates)):
                if a in associates[i] or b in associates[i]:
                    associates[i].add(a + 1)
                    associates[i].add(b + 1)
                    visited[a] = True
                    visited[b] = True
                    tag = True
            if tag == False:
                temp = set()
                temp.add(a + 1)
                temp.add(b + 1)
                visited[a] = True
                visited[b] = True
                associates.append(temp)

for callPair in associates:
    callPair = list(callPair)
    callPair.sort()
    callPair = [str(c) for c in callPair]
    print(' '.join(callPair))

for i in range(len(suspectList)):
    if visited[suspectList[i] - 1] == False:
        print(suspectList[i])