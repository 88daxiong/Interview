'''
@Descripttion: 
@Author: daxiong
@Date: 2019-08-31 15:01:27
@LastEditors: daxiong
@LastEditTime: 2019-09-06 15:22:03
'''
N = int(input().strip())

resNum = list()
for i in range(N):
    s = input().strip().split()
    name = s[0]
    studyId = s[1]
    grade = int(s[2])
    resNum.append((grade, name, studyId))

resNum.sort()
print("{0} {1}".format(resNum[-1][1], resNum[-1][2]))
print("{0} {1}".format(resNum[0][1], resNum[0][2]))
