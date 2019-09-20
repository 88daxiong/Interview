'''
@Descripttion: 香蕉问题
@Author: daxiong
@Date: 2019-09-19 19:08:21
@LastEditors: daxiong
@LastEditTime: 2019-09-19 19:20:17
'''
def getNumOfBananas(num, rounds):
    print(num)
    if rounds == 5:
        return num
    else:
        num = num * 5 + 1
        return getNumOfBananas(num, rounds + 1)

print(getNumOfBananas(1, 1))
    