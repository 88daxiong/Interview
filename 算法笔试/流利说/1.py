'''
@Descripttion: 
@Author: daxiong
@Date: 2019-09-11 21:04:38
@LastEditors: daxiong
@LastEditTime: 2019-09-12 09:17:50
'''
import sys
line = sys.stdin.readline().strip()
while line:
    line = line.replace('[', '').replace(']', '')
    line = [int(x) for x in line.split(',')]
    N = int(len(line) ** 0.5)
    print(N)
    
    line = sys.stdin.readline().strip()


# [[0, 1, 0], [0, 0, 1], [1, 0, 0]]
# [[0, 0, 0, 1, 0], [1, 0, 0, 0, 0], [0, 0, 0, 1, 1], [0, 0, 0, 0, 0], [0, 1, 0, 0, 0]]