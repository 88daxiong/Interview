'''
@Descripttion: 
@Author: daxiong
@Date: 2019-08-03 14:34:49
@LastEditors: daxiong
@LastEditTime: 2019-08-17 19:52:56
'''
#coding=utf-8
# 本题为考试多行输入输出规范示例，无需提交，不计分。
import sys

if __name__ == "__main__":
    # 读取第一行的n
    n = int(sys.stdin.readline().strip())
    line = sys.stdin.readline().strip()
    values = map(int, line.split())
    result = list()
    for v in values:
        result.append(n + 1 - v)
    result = [str(x) for x in result]
    print((' '.join(result)))