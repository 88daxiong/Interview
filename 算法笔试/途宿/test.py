'''
@Descripttion: ASCII排序
@Author: daxiong
@Date: 2019-09-06 21:20:36
@LastEditors: daxiong
@LastEditTime: 2019-09-06 21:25:55
'''
s = input().strip()
visited = [False for _ in range(len(s))]
strC = list()

for i in range(len(s)):
    if s[i].isalpha():
        strC.append(s[i])
        visited[i] = True

s = list(s)
strC.sort(reverse = True)
for i in range(len(s)):
    if visited[i] == True:
        s[i] = strC.pop(-1)

print(''.join(s))
