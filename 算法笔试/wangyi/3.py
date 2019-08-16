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
        result.append(v)
    temp1 = [x for x in result if x % 2 == 0]
    temp2 = [x for x in result if x %2 != 0]
    if temp1 != [] or temp2  != []:
        result.sort()
    result = [str(x) for x in result]
    print((' '.join(result)))