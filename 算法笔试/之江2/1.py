'''
@Descripttion: 验证素数
@Author: daxiong
@Date: 2019-09-06 15:47:53
@LastEditors: daxiong
@LastEditTime: 2019-09-06 16:52:49
'''

def isPrime(num):
    if num >= 1:
        if num == 2:
            return True
        if num % 2 == 0:
            return False
        else:
            cur = 3
            while cur ** 2 <= num:
                if num % cur == 0:
                    return False
                cur += 2
            return True
    return False

N = int(input().strip())

a, b = 0, 0
for a in range(2, int(N / 2) + 1):
    b = N - a 
    if isPrime(a) == True and isPrime(b) == True:
        break
print("{0} {1}".format(min(a, b), max(a, b)))



