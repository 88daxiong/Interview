'''
@Descripttion: 
@Author: daxiong
@Date: 2019-09-17 20:09:57
@LastEditors: daxiong
@LastEditTime: 2019-09-17 21:14:43
'''
s = input().strip().split()
a1, a2, a3, a4, N = int(s[0]), int(s[1]), int(s[2]), int(s[3]), int(s[4])

const = 10**9 + 7
arr = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]
index = 5
while index <= N:
    for j in range(4):
        a = ((index - 1) % 4 + 3) % 4
        b = ((index - 3) % 4 + 3) % 4
        c = ((index - 4) % 4 + 3) % 4
        x = (index % 4 + 3) % 4
        arr[x][j] = arr[a][j] + arr[b][j] + arr[c][j]
    
    index += 1
resNum = a1 * arr[x][0] + a2 * arr[x][1] + a3 * arr[x][2] + a4 * arr[x][3]
print(resNum%const)