'''
@Descripttion: 
@Author: daxiong
@Date: 2019-09-24 15:58:11
@LastEditors: daxiong
@LastEditTime: 2019-09-24 16:29:28
'''
N = int(raw_input().strip())
# N = 10
S = N - 2
matrix = [[' ' for i in range(4*S-2)] for _ in range(N)]


for i in range(S):
    if i == 0:
        matrix[i][S-1] = '*'
        matrix[i][3*S-2] = '*'
    elif i == 1:
        x = [S - 2, 3*S-3]
        for j in x:
            for k in range(3):
                matrix[i][j + k] = '*'
    else:
        x = [S - i - 1, S + i - 2, 3*S - i-2, 3*S + i - 3]
        for j in x:
            for k in range(2):
                matrix[i][j + k] = '*'

matrix[S][:] = ['*' for i in range((4*S-2))]
matrix[S+1][1:-1] = ['*' for i in range((4*S-4))]
for row in matrix:
    print(''.join(row))


