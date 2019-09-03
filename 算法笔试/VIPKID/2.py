'''
@Descripttion: 移动平均数
@Author: daxiong
@Date: 2019-09-03 15:55:51
@LastEditors: daxiong
@LastEditTime: 2019-09-03 17:09:19
'''
arr = input().strip().split()
arr = [int(i) for i in arr]
k = int(input().strip())

if k == 0:
    print(0)
else:
    resNum = list()
    curStr = arr[:k]
    resNum.append(float(sum(curStr))/k)
    begin = arr[0]
    for i in range(k, len(arr)):
        resNum.append(float(resNum[-1]*k - begin + arr[i])/k)
        begin = arr[i - k + 1]

    print('%.2f'%resNum[0],  end=' ')
    for i in range(1, len(resNum) - 1):
        print('%.2f'%resNum[i], end=' ')
    print('%.2f'%resNum[-1], end = ' ')