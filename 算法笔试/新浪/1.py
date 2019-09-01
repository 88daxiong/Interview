'''
@Descripttion: 算法开发
@Author: daxiong
@Date: 2019-08-31 15:56:23
@LastEditors: daxiong
@LastEditTime: 2019-08-31 17:00:43
'''
# s = input().strip().split(',')
# s = [int(x) for x in s]
s = [1, 2, 3, 4, 5]
s.sort()
resNum = 0
end = len(s) - 1
begin = 0
while end > begin:
    if end > begin and s[end] > s[begin] + end - begin:
        end -= 1
    else:
        break
temp = [s[begin] + i + 1 for i in range(end - begin)]
resNum = sum(temp) - sum(s[begin + 1: end + 1])
print(resNum)