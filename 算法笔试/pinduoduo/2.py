#coding=utf-8
import sys 
if __name__ == "__main__":
    # array = sys.stdin.readline().strip()
    # array = list(map(str, array.split()))
    res = list()
    array = ['CAC','CPC']
    for index in range(len(array) - 1):
        res.append(list(set(array[index]) & set(array[index + 1])))
    res.append(list(set(array[0]) & set(array[-1])))
    if [] in res:
        print("false")
    if len(array) == 2:
        if len(res[0]) == 1 and array[0].count(res[0][0]) == 1:
            print('false')
        else:
            print('true')

    


# 这题目用广度搜索试一试