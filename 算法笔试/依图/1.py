'''
@Descripttion: 水源出水
@Author: daxiong
@Date: 2019-09-20 19:01:10
@LastEditors: daxiong
@LastEditTime: 2019-09-20 19:57:27
'''
N = int(input().strip()) # 几组测试数据
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

for round in range(N):
    print("Case #{}:".format(round + 1))
    s = input().strip().split()
    n, m, a, b, c = int(s[0]), int(s[1]), int(s[2]), int(s[3]), int(s[4])

    matrix = [[0 for column in range(m)] for row in range(n)]
    visited = [[False for column in range(m)] for row in range(n)]
    stack = list()
    stack.append(([a, b], c))
    matrix[a][b] = c
    visited[a][b] = True

    while stack != []:
        [a, b], c = stack.pop(0)
        for direct in directions:
            newA = a + direct[0]
            newB = b + direct[1]
            if 0 <= newA < n and 0 <= newB < m and visited[newA][newB] == False and c >= 1:
                matrix[newA][newB] = c - 1
                visited[newA][newB] = True
                stack.append(([newA, newB], c - 1))
    
    for rows in matrix:
        rows = [str(val) for val in rows]
        print(' '.join(rows))                
        
# n行，m列；BFS解题