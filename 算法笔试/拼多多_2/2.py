'''
@Descripttion: 扑克游戏
@Author: daxiong
@Date: 2019-09-01 14:54:41
@LastEditors: daxiong
@LastEditTime: 2019-09-01 19:45:22
'''
round = int(input().strip()) # 存储轮数

nList = list() # 存储小梅的序列
mList = list() # 存储小白的序列
for i in range(round):
    s = input().strip()
    nTemp = [int(x) for x in s]
    nList.append(nTemp)

    s = input().strip()
    mTemp = [int(x) for x in s]
    mList.append(mTemp)

allops = []

def dfs(nArray, newArray, mArray, operators):
    if newArray == mArray:
        if operators not in allops:
            allops.append(operators)
        return
    for i in range(len(nArray)):
        dfs(nArray[1: ], newArray, mArray, operators + ['d'])
        dfs(nArray[1: ], [nArray[0]] + newArray, mArray, operators + ['l'])
        dfs(nArray[1: ],  newArray + [nArray[0]], mArray, operators + ['r'])


for i in range(round):
    nArray = nList[i]
    mArray = mList[i]
    N = len(nArray)
    M = len(mArray)
    
    print("{")
    dfs(nArray, [], mArray, [])
    allops.sort()
    for op in allops:
        op = ' '.join(op)
        print(op)
    print("}")
    allops = []