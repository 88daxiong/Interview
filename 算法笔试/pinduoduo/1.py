#coding=utf-8
import sys 
if __name__ == "__main__":
    num1 = sys.stdin.readline().strip()
    num2 = sys.stdin.readline().strip()
    num1 = list(map(int, num1.split()))
    num2 = list(map(int, num2.split()))

    index = 0
    num2.sort()
    tag = False
    while index < len(num1) - 1:
        if num1[index] > num1[index + 1]:
            break
        index += 1
    if index == 0: #第一个
        a = num1[index]
        b = num1[1]
        if len(num1) == 2:
            j = len(num2) - 1
            while j >= 0:
                if num2[j] > a:
                    num1[1] = num2[j]
                    tag = True
                    break
                if num2[j] < b:
                    num1[0] = num2[j]
                    tag = True
                    break
                j -= 1
        else:
            c = num1[2] # 这个时候需要找到比c小，然后或者比a大，或者比b小的数;
            j = len(num2) - 1
            while j >= 0:
                if num2[j] > a and num2[j] < c:
                    num1[1] = num2[j]
                    tag = True
                    break
                if num2[j] < b:
                    num1[0] = num2[j]
                    tag = True
                    break
                j -= 1
    elif index == len(num1) - 2: #最后一个
        a = num1[-2]
        b = num1[-1]
        j = len(num2) - 1
        while j >= 0:
            if num2[j] > a:
                num1[-1] = num2[j]
                tag = True
                break
            if num2[j] < b:
                num1[-2] = num2[j]
                tag = True
                break 
            j -= 1
    else: #在中间
        a = num1[index-1]
        b = num1[index]
        c = num1[index+1]
        d = num1[index+2]
        j = len(num2) - 1
        while j >= 0:
            if num2[j] > b and num2[j] < d:
                num1[index + 1] = num2[j]
                tag = True
                break 
            if num2[j] > a and num2[j] < c:
                num1[index] = num2[j]
                tag = True
                break
            j -= 1
    if tag:
        num1 = [str(i) for i in num1]
        num1 = ' '.join(num1)
        print(num1)
    else:
        print("NO")

        
        

            


# 然后现在需要找到的数字是需要在index-1和index+2之间的；
# 其中如果a = -1,说明是第一个
# 如果d = len(num1),说明是最后一个
# 只有是这两种情况下，才不需要判断

