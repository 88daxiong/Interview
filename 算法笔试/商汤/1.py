'''
@Descripttion: 字符串分类
@Author: daxiong
@Date: 2019-09-21 19:11:40
@LastEditors: daxiong
@LastEditTime: 2019-09-21 19:47:08
'''
N = int(input().strip())
allStr = list()

for i in range(N):
    s = input().strip()
    s = list(s)
    s.sort()
    if s not in allStr:
        allStr.append(s)

print(len(allStr))    