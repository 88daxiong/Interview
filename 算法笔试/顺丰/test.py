'''
@Descripttion: 
@Author: daxiong
@Date: 2019-08-29 20:52:28
@LastEditors: daxiong
@LastEditTime: 2019-08-29 21:02:05
'''

def union_find(nodes, edges):
    father = [0]*len(nodes)     # 记录父节点
    for node in nodes:  # 初始化为本身
        father[node] = node

    for edge in edges:  # 标记父节点
        head = edge[0]
        tail = edge[1]
        father[tail] = head

    for node in nodes:
        while True:         # 循环，直到找到根节点
            father_of_node = father[node]
            if father_of_node != father[father_of_node]:
                father[node] = father[father_of_node]
            else:           # 如果该节点的父节点与其爷爷节点相同，
                break       # 则说明找到了根节点

    L = {}
    for i, f in enumerate(father):
        L[f] = []
    for i, f in enumerate(father):
        L[f].append(i)

nodes = list(range(0, 10))
test_edges = [[0, 1], [0, 4], [1, 2], [1, 3], [5, 6], [6, 7], [7, 5], [8, 9]]

L = union_find(nodes, test_edges)
print(L)