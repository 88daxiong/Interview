'''
@Descripttion: 最多的整块个数
@Author: daxiong
@Date: 2019-08-19 15:41:02
@LastEditors: daxiong
@LastEditTime: 2019-08-19 16:02:15
'''

def maxBox(n):
    res = 0
    nsqure = n ** 2

    for i in range(1, n):
        temp = nsqure - i ** 2
        res += int(temp ** 0.5)
    
    return res * 4

print(maxBox(3))