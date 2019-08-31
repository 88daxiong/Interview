#coding=utf-8
'''
@Descripttion: 任务题
@Author: daxiong
@Date: 2019-08-30 19:57:46
@LastEditors: daxiong
@LastEditTime: 2019-08-30 20:34:59
'''
import itertools
# limited = int(input())
# minNum = int(input())
# maxNum = int(input())
# strA = raw_input().strip().split(',')
# strB = raw_input().strip().split(',')

limited = 1
minNum = 3
maxNum = 5
strA = ['weather', 'joke', 'music', 'stock', 'joke', 'news', 'taxi', 'temperature', 'pm2.5']
strB = ['joke', 'music', 'news', 'stock', 'joke', 'joke', 'news', 'taxi']

allA = list(itertools.permutations(strA))
print(allA)

def cut2(s, minNum, maxNum):
    results = []

    # x + 1 表示子字符串长度
    for x in range(minNum, maxNum + 1):
        # i 表示偏移量
        for i in range(len(s) - x):
            if x == 0:
                results.append(s[i:i + x + 1])
            elif x < 2:
                for j in range(len(s) - x - i):
                    results.append(s[i] + s[j + x + i])
            else:
                for j in range(len(s) - x - i):
                    results.append(s[i:i+x] + s[j + x + i])

print(cut2(strA, minNum, maxNum))



