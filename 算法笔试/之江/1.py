'''
@Descripttion: 性感素数
@Author: daxiong
@Date: 2019-09-02 15:05:30
@LastEditors: daxiong
@LastEditTime: 2019-09-03 15:34:25
'''
import math

def is_prime(number):
    if number > 1:
        if number == 2:
            return True
        if number % 2 == 0:
            return False
        for i in range(3, int(math.sqrt(number) + 1), 2):
            if number % i == 0:
                return False
        return True
    return False

s = int(input().strip())
tag = False
if is_prime(s) == True:
    print("YES")
    if is_prime(s - 6) == True:
        m = s - 6
        tag = True
    elif is_prime(s + 6) == True:
        m = s + 6
        tag = True
    if tag == True:
        print(m)
else:
    print("NO")
    while tag == False:
        if is_prime(s) == True:
            if is_prime(s + 6) == True or is_prime(s - 6) == True:
                tag = True
        s += 1
    print(s - 1)
        
