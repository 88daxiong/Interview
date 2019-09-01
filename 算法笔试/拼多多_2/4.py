'''
@Descripttion: 
@Author: daxiong
@Date: 2019-09-01 14:54:47
@LastEditors: daxiong
@LastEditTime: 2019-09-01 17:05:49
'''
s = input().strip().split()
n, m, k = int(s[0]), int(s[1]), int(s[2])
# d = k

m, n, k = 5, 3, 5
d = k

stack = list()
stack.append([m*n, m, n]) # 最大值
k -= 1
cur = 0
visited = list()
visited.append([m, n])

while k > 0:
    stack.sort(reverse = True)
    s = stack.pop(0)
    cur += 1
    a ,b = s[1], s[2]
    if a - 1 >= 1 and [a-1, b] not in visited:
        stack.append([(a-1)*b, a - 1, b])
        visited.append([a-1, b])
        k -= 1
    if b -1 >= 1 and [a, b-1] not in visited:
        stack.append([(b-1)*a, a, b - 1])
        visited.append([a, b-1])
        k -= 1
stack.sort(reverse = True)
print(stack[d - cur - 1][0])
    

