'''
@Descripttion: 
@Author: daxiong
@Date: 2019-08-17 19:48:39
@LastEditors: daxiong
@LastEditTime: 2019-08-18 10:14:20
'''
import sys

def check(result, num, direction): # 1,2,3,4分别表示这个点的上下左右。需要判断是否能行
    tag = False
    if direction == 1:
        if num[0] - 1 >= 0 and result[num[0] - 1][num[1]] > 0:
            tag = True
    elif direction == 2:
        if num[0] + 1 < len(num) and result[num[0] + 1][num[1]] > 0:
            tag = True
    elif direction == 3:
        if num[1] - 1 >= 0 and result[num[0]][num[1] - 1] > 0:
            tag = True
    else:
        if num[1] + 1 < len(result[0]) and result[num[0]][num[1] + 1] > 0:
            tag = True
    return tag

if __name__ == "__main__":
    t = int(sys.stdin.readline().strip())
    N = list()
    M = list()
    End1 = list()
    End2 = list()
    Begin1 = list()
    Begin2 = list()
    Result = list()
    for i in range(t):
        a = sys.stdin.readline().strip()
        a = list(map(int, a.split()))
        n, m = int(a[0]), int(a[1]) # n表示行，m表示列
        N.append(N)
        M.append(M)
    
        result = list() # 存储这个数组，在这里我把X记为1，.记为2
        for j in range(n):
            line = sys.stdin.readline().strip()
            values = line
            temp = list()
            for c in values:
                if c == '.':
                    temp.append(1)
                else:
                    temp.append(0)
            result.append(temp)
        Result.append(result)
        
        a = list(map(int, sys.stdin.readline().strip().split()))
        beginN, beginM = int(a[0]) - 1, int(a[1]) - 1 # n表示行，m表示列
        a = list(map(int, sys.stdin.readline().strip().split()))
        endN, endM = int(a[0]) - 1, int(a[1]) - 1 # n表示行，m表示列
        Begin1.append(beginN)
        Begin2.append(beginM)
        End1.append(endN)
        End2.append(endM)
    
    for i in range(t):
        n = N[i]
        m = M[i]
        beginN = Begin1[i]
        beginM = Begin2[i]
        endN = End1[i]
        endM = End2[i]
        result = Result[i]

        if result[endN][endM] == 1:
            print("YES")
        else:
            # 直接判断如果上下左右全是1的话，就没办法了
            end = (endN, endM)
            tag = 1
            if check(result, end, 1):
                tag *= result[end[0] - 1][end[1]]
            if check(result, end, 2):
                tag *= result[end[0] + 1][end[1]]
            if check(result, end, 3):
                tag *= result[end[0]][end[1] - 1]
            if heck(result, end, 4):
                tag *= result[end[0]][end[1] + 1]
            if tag >= 1:
                print("YES")
            else:
                print("NO")
            # end = (endN, endM)
            # stack = list()
            # if check(result, end, 1) == True:
            #     stack.append((end[0] - 1, end[1]))
            #     result[end[0] - 1][end[1]] -= 1
            # if check(result, end, 2) == True:
            #     stack.append((end[0] + 1, end[1]))
            #     result[end[0] + 1][end[1]] -= 1
            # if check(result, end, 3) == True:
            #     stack.append((end[0], end[1] - 1))
            #     result[end[0]][end[1] - 1] -= 1
            # if check(result, end, 4) == True:
            #     stack.append((end[0], end[1] + 1))
            #     result[end[0]][end[1] + 1] -= 1
            # tag = False
            # index = 0
            # print(result)
            # while stack != []:
            #     print(stack)
            #     temp = stack.pop(0)
            #     if temp == end:
            #         tag = True
            #         break
            #     if check(result, temp, 1) == True:
            #         stack.append((temp[0] - 1, temp[1]))
            #         result[temp[0] - 1][temp[1]] -= 1
            #     if check(result, temp, 2) == True:
            #         stack.append((temp[0] + 1, temp[1]))
            #         result[temp[0] + 1][temp[1]] -= 1
            #     if check(result, temp, 3) == True:
            #         stack.append((temp[0], temp[1] - 1))
            #         result[temp[0]][temp[1] - 1] -= 1
            #     if check(result, temp, 4) == True:
            #         stack.append((temp[0], temp[1] + 1))
            #         result[temp[0]][temp[1] + 1] -= 1
            # if tag == True:
            #     print("YES")
            # else:
            #     print("NO")
            # print(result)



# 需要往上下左右四个方向走，走完一个该方向上的数字减1，如果为0则不能再走列。
# 判断是都有这样的数字可以走，BFS？,对的，使用BFS一定可以做,也就是是不是可以两遍走到。