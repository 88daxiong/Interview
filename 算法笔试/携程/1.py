'''
@Descripttionl 车辆时刻表分组 
@Author: daxiong
@Date: 2019-09-04 19:13:54
@LastEditors: daxiong
@LastEditTime: 2019-09-04 19:50:04
'''
strL = input().strip()
numList = list() # 存放每一组的值
limited = dict() # 存放是否符合条件
curLength = 0

for c in strL:
    if c in limited:
        limited[c] -= 1
        if limited[c] == 0:
            del limited[c]
        if limited == dict():
            numList.append(curLength + 1)
            curLength = 0
        else:
            curLength += 1
    else:
        limited[c] = strL.count(c) - 1
        if limited[c] == 0:
            del limited[c]
        if limited == dict():
            numList.append(curLength + 1)
            curLength = 0
        else:
            curLength += 1
numList = [str(x) for x in numList]
print(','.join(numList))

# 也即出现在这个组的数据c,所有c都必须放在这一组里面