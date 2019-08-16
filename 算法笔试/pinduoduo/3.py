#coding=utf-8
import sys 
if __name__ == "__main__":
    # line = sys.stdin.readline().strip()
    # N, M = map(int, line.split())[0], map(int, line.split())[1] # N，任务个数; M,依赖关系
    # line = sys.stdin.readline().strip()
    # time = map(int, line.split()) # 每个任务耗费的时间
    # depend = list()
    # for i in range(M):
    #     line = sys.stdin.readline().strip()
    #     depend.append(map(int, line.split()))
    N, M = 5, 6
    time = [1,2,1,1,1]
    depend = [[1,2],[1,3],[1,4],[2,5],[3,5],[4,5]] # 这是有依赖关系的      f
    depend.sort(key = lambda x:(-x[1], -x[0]))
    res = dict()
    for pair in depend:
        if pair[1] not in res:
            res[pair[1]] = list()
        res[pair[1]].append(pair[0])
    


# 首先按照依赖关系排一个顺序,然后在不改变依赖关系的条件下，将这些数组按照时间进行一个从小到大的排序；
# 然后按照时间从小到大将不存在依赖关系的依次插入到数组中；


