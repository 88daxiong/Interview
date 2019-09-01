'''
@Descripttion: 
@Author: daxiong
@Date: 2019-08-31 15:01:27
@LastEditors: daxiong
@LastEditTime: 2019-09-01 20:47:33
'''
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

print(getC(5,0))