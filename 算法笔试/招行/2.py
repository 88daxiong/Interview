'''
@Descripttion: 
@Author: daxiong
@Date: 2019-09-24 15:58:15
@LastEditors: daxiong
@LastEditTime: 2019-09-24 16:41:49
'''
s = raw_input().strip().split(',')
s = [int(x) for x in s ]

visited = [False for val in range(len(s))]
resNum = 0
for i in range(len(s)):
    if s[i] == 1:
        visited[i] = True
        if i -1 >= 0 and s[i - 1] == 0:
            visited[i - 1] = True
        if i + 1 < len(s) and s[i + 1] == 0:
            visited[i + 1] = True
    if s[i] == 2:
        visited[i] = True
        if i - 1 >= 0 and s[i - 1] == 0:
            visited[i - 1] = True
        if i - 2 >= 0 and s[i - 2] == 0:
            visited[i - 2] = True
        if i + 1 < len(s) and s[i + 1] == 0:
            visited[i + 1] = True
        if i + 2 < len(s) and s[i + 2] == 0:
            visited[i + 2] = True

for i in range(len(s)):
    if visited[i] == True:
        continue
    else:
        visited[i] = True
        if i + 1 < len(s) and s[i + 1] == 0:
            visited[i + 1] = True
        resNum += 1

print(resNum)