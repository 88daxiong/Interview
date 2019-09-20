'''
@Descripttion: 
@Author: daxiong
@Date: 2019-09-19 16:59:42
@LastEditors: daxiong
@LastEditTime: 2019-09-19 17:50:38
'''
N = int(input().strip())
resNum = 1
while N / 2 != 0:
    resNum += 1
    N = int(N / 2)
    print(N)

def factorial(n):
    result = n;
    for i in range(1,n):
        result *= i
        if result > 1000003:
            result %= 1000003
    return result

print(factorial(resNum))