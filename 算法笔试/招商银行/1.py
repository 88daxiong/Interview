'''
@Descripttion: 小招喵的机器人
@Author: daxiong
@Date: 2019-09-15 21:10:43
@LastEditors: daxiong
@LastEditTime: 2019-09-15 21:49:33
'''
strL = input().strip()
lenth = len(strL)
resList = [str(0) for x in strL]

begin = 0 # 起始点 一定是R
end = 0 # 结束点 一定是L
Rpositions = 0 # R的位置
Lpositions = 0 # L的位置

index = 0
while index < lenth:
    numR = 0
    numL = 0
    begin = index
    while strL[index] == 'R':
        index += 1
    Rpositions = index - 1
    Lpositions = index
    while index < lenth and strL[index] == 'L':
        index += 1
    end = index - 1
    # print(begin, Rpositions, Lpositions, end)
    numR = int((Rpositions - begin) / 2) + int((end - Rpositions) / 2) + 1
    numL = int((Lpositions - begin) / 2) + int((end - Lpositions) / 2)+ 1
    resList[Rpositions] = str(numR)
    resList[Lpositions] = str(numL)
    # print(numR, numL)

print(' '.join(resList))