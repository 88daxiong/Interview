'''
@Descripttion: 
@Author: daxiong
@Date: 2019-09-15 20:30:18
@LastEditors: daxiong
@LastEditTime: 2019-09-15 22:42:51
'''
n = input()
ans = [1]* len(n)
if len(n) == 2:
    print('1 1')
else:
    for i in range(1, len(n)-1):
        if n[i] == 'R' and n[i-1] == 'R':
            ans[i+1] += ans[i-1]
            ans[i-1] = 0
    for j in range(len(n)-2, 0, -1):
        if n[j] == 'L' and n[j+1] == 'L':
            ans[j-1] += ans[j+1]
            ans[j+1] = 0
    print(' '.join(str(i) for i in ans))