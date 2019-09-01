'''
@Descripttion: 优先偶数TopN序
@Author: daxiong
@Date: 2019-09-01 14:54:37
@LastEditors: daxiong
@LastEditTime: 2019-09-01 15:12:29
'''
s = input().strip().split(',')
s[-1], N = s[-1].split(';')[0], int(s[-1].split(';')[1])
a = [int(x) for x in s if int(x) % 2 == 0]
b = [int(x) for x in s if int(x) % 2 != 0]
a.sort(reverse = True)
b.sort(reverse = True)
resList = list()
if len(a) >= N:
    resList = a[: N]
else:
    resList = a + b[: N - len(a)]

resList = [str(x) for x in resList]
print(','.join(resList))