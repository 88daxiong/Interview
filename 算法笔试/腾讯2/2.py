'''
@Descripttion: 花匠小Q
@Author: daxiong
@Date: 2019-09-01 20:28:08
@LastEditors: daxiong
@LastEditTime: 2019-09-01 22:19:41
'''
# s = input().strip().split()
# t, k = int(s[0]), int(s[1])
t = 1
k = 2


def getValue(n):
    if n <= 1:
        return 1
    else:
        return n*getValue(n-1)

def getC(n, m):
    first = getValue(n)
    second = getValue(m)
    third = getValue(n - m)
    return int(first/(second*third))


for i in range(t):
    # s = input().strip().split()
    # a, b = int(s[0]), int(s[1])

    a, b = 3,3

    resNum = 0
    for flower in range(a, b + 1): #  摆flower朵花
        c = int(flower / k) # 表示最多有这么多组白花；
        for j in range(c + 1):
            resNum += getC(flower-j*k+j, j)
            
    print(resNum)
        

