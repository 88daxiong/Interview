'''
@Descripttion: 
@Author: daxiong
@Date: 2019-08-17 19:48:50
@LastEditors: daxiong
@LastEditTime: 2019-08-17 20:05:05
'''
import sys 
for line in sys.stdin:
    a = line.split()
    print(int(a[0]) + int(a[1]))


import sys
if __name__ == "__main__":
    # 读取第一行的n
    n = int(sys.stdin.readline().strip())
    ans = 0
    for i in range(n):
        # 读取每一行
        line = sys.stdin.readline().strip()
        # 把每一行的数字分隔后转化成int列表
        values = list(map(int, line.split()))
        for v in values:
            ans += v
    print(ans)