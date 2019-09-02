'''
@Descripttion: 
@Author: daxiong
@Date: 2019-09-02 15:20:00
@LastEditors: daxiong
@LastEditTime: 2019-09-02 16:03:31
'''
s = input().strip().split()
n, m = int(s[0]), int(s[1])

egde = list()
for i in range(m):
    s = input().strip().split()
    egde.append([int(s[0]), int(s[1])])

k = int(input().strip())

while k > 0:
    nodeColor = [0 for i in range(10010)]
    color = set()
    s = input().strip().split()
    for i in range(n):
        nodeColor[i] = int(s[i])
        color.add(nodeColor[i])
    
    tag = True
    for j in range(m):
        if nodeColor[egde[j][0]] == nodeColor[egde[j][1]]:
            tag = False
            break

    if tag == True:
        print("{0}-coloring".format(len(color)))
    else:
        print("No")
    
    k -= 1