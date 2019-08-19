'''
@Descripttion: 
@Author: daxiong
@Date: 2019-08-17 19:48:34
@LastEditors: daxiong
@LastEditTime: 2019-08-17 22:01:32
'''
import sys
if __name__ == "__main__":
    a = sys.stdin.readline().strip()
    a = list(map(int, a.split()))
    n, k = int(a[0]), int(a[1])
    line = sys.stdin.readline().strip()
    values = list(map(int, line.split()))

    # n, k = 7, 3
    # values = [1, 2, 6, 1, 1, 7, 1]
    
    temp = values[: k]
    num = sum(temp)
    result = list()
    
    for i in range(1, n - k + 1):
        result.append(num)
        num -= temp[0]
        del temp[0]
        temp.append(values[(i + k - 1)%n])
        num += temp[-1]
    print(result.index(min(result)) + 1)