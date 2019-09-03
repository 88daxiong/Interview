'''
@Descripttion: 迷宫游戏
@Author: daxiong
@Date: 2019-09-03 18:55:37
@LastEditors: daxiong
@LastEditTime: 2019-09-03 20:46:31
'''
N = int(input().strip())
matrix = list()
for i in range(N):
    rows = list(input().strip())
    if 'S' in rows: # 起始点
        begin = [i, rows.index('S')]
    if 'E' in rows: # 结束点
        end = [i, rows.index('E')]
        rows[rows.index('E')] = '.'
    matrix.append(rows)

visited = [[False for _ in a] for a in matrix]
stack = list()
stack.append((begin, 0))

find = False
while stack != []:
    [a, b], depth = stack.pop(0)
    if [a, b] == end:
        find = True
        break
    if matrix[(a - 1 + N) % N][b] == '.' and visited[(a - 1 + N) % N][b] == False: # 向左移
        stack.append(([(a - 1 + N) % N, b], depth + 1))
        visited[(a - 1 + N) % N][b] = True

    if matrix[(a + 1 + N) % N][b] == '.' and visited[(a + 1 + N) % N][b] == False: # 向右移
        stack.append(([(a + 1 + N) % N, b], depth + 1))
        visited[(a + 1 + N) % N][b] = True
        
    if matrix[a][(b - 1 + N) % N] == '.' and visited[a][(b - 1 + N) % N] == False: # 向上移
        stack.append(([a, (b - 1 + N) % N], depth + 1))
        visited[a][(b - 1 + N) % N] = True

    if matrix[a][(b + 1 + N) % N] == '.' and visited[a][(b + 1 + N) % N] == False: # 向上移
        stack.append(([a, (b + 1 + N) % N], depth + 1))
        visited[a][(b + 1 + N) % N] = True

if find == True:
    print(depth)
else:
    print(-1)

# 注意设置visited数组
# 在BFS的时候用深度来表示