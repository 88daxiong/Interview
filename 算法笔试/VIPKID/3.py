'''
@Descripttion: 
@Author: daxiong
@Date: 2019-09-25 20:34:43
@LastEditors: daxiong
@LastEditTime: 2019-09-25 20:34:43
'''
C = int(input())

for c in range(C):
    n = int(input())
    mis = list(map(int, input().split(" ")))
    max_pow = 0
    power = [0]*n
    
    for i in range(1, n):
        cur = power[i-1]
        for j in range(i):
            if mis[j] < mis[i]:
                cur += 1
            elif mis[j] > mis[i]:
                cur -= 1
        max_pow = max(max_pow, cur)
        power[i] = cur
    
    print(str(max_pow)+" "+str(power[-1]))