'''
@Descripttion: 0,1背包问题
@Author: daxiong
@Date: 2019-09-06 20:32:01
@LastEditors: daxiong
@LastEditTime: 2019-09-06 20:49:42
'''
s = input().strip().split()
n, m = int(s[0]), int(s[1])
packet = list()

for i in range(n):
    s = input().strip().split()
    w, v = int(s[0]), int(s[1])
    packet.append((float(v) / w, v, w))

packet.sort(key = lambda x: -x[0]) # 按照性价比排序

resValue = 0
for c in packet:
    v, w = c[1], c[2]
    if w > m:
        break
    else:
        resValue += v
        m -= w
print(resValue)
