'''
@Descripttion: 寻找子串
@Author: daxiong
@Date: 2019-08-31 17:30:26
@LastEditors: daxiong
@LastEditTime: 2019-09-05 21:35:24
'''

s = input().strip()
s = [_ for _ in s]
p = set(s)
maxNum = 0
for c in p:
    if s.count(c) > maxNum:
        maxNum = s.count(c)

print(maxNum)

# 最多的就是单个字符