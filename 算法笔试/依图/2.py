'''
@Descripttion: 矩阵操作
@Author: daxiong
@Date: 2019-09-20 19:01:16
@LastEditors: daxiong
@LastEditTime: 2019-09-20 19:41:34
'''
def multiply(matrixA, matrixB, matrixC): # 矩阵乘法操作
    for i in range(len(matrixC)):
        for j in range(len(matrixC[i])):
            a = 0
            b = 0
            while (a < len(matrixA[i])) and (b < len(matrixB)):
                matrixC[i][j] += matrixA[i][a] * matrixB[b][j]
                a += 1
                b += 1
    return

def transpose(matrixA): # 转置操作
    return list(zip(*matrixA))

s = input().strip().split()
n, m = int(s[0]), int(s[1])
matrixA = [[0 for column in range(m)] for row in range(n)]
matrixB = [[0 for column in range(m)] for row in range(n)]

for i in range(n):
    s = input().strip().split()
    s = [int(x) for x in s]
    matrixA[i][:] =s

for i in range(n):
    s = input().strip().split()
    s = [int(x) for x in s]
    matrixB[i][:] = s

matrixA = transpose(matrixA) # A的转置
matrixC = [[0 for column in range(m)] for row in range(m)] # 第一次乘完，C为m*m
multiply(matrixA, matrixB, matrixC)

matrixB = transpose(matrixB) # B的转置
maxtrixD = [[0 for column in range(n)] for row in range(m)]
multiply(matrixC, matrixB, maxtrixD)

maxtrixD = transpose(maxtrixD) # 最后的输出

n_c, m_c = len(maxtrixD), len(maxtrixD[0])
print("{0} {1}".format(n_c, m_c))

for rows in maxtrixD:
    rows = [str((val % 1009)) for val in rows]
    print(' '.join(rows))  
