'''
@Descripttion: 交换纸牌游戏
@Author: daxiong
@Date: 2019-08-19 15:59:14
@LastEditors: daxiong
@LastEditTime: 2019-08-19 16:02:10
'''
def change(A, B):
    sumA = sum(A)
    sumB = sum(B)
    average = int((sumA + sumB) / 2)
    res = list()

    for num in A:
        if average + num - sumA in B:
            res.append(num)
            res.append(average + num - sumA)
            break

    return res

A = [1, 3, 4]
B = [2, 2]
print(change(A, B))