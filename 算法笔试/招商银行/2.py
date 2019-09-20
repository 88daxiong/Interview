'''
@Descripttion: 
@Author: daxiong
@Date: 2019-09-15 20:30:15
@LastEditors: daxiong
@LastEditTime: 2019-09-15 22:22:35
'''
strL = input().strip()
strL = strL[::-1]

resNum = 0
dp = [[0 for i in range(10)] for j in range(len(strL))]

for i in range(len(strL)):
    if strL[i] == '?':
        for j in range(10):
            if i == 0:
                dp[0][j] = (j + 8) % 13
            else:
                dp[i][j] = (dp[i - 1][j] + j * 10 +8 ) % 13
    else:
        c = int(strL[i])
        for j in range(10):
            dp[i][j] = (dp[i - 1][j] + c * 10 + 8) % 13

print(dp)


# 2??