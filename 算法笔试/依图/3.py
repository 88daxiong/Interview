'''
@Descripttion: 计数V2.0
@Author: daxiong
@Date: 2019-09-20 19:01:20
@LastEditors: daxiong
@LastEditTime: 2019-09-20 22:03:01
'''
T = int(input().strip())

for round in range(T):
    s = input().strip().split()
    n, m = int(s[0]), int(s[1])
    points = [int(val) for val in input().strip().split()]
    points = [[val, index, 0] for index, val in enumerate(points)]
    points.sort()
    intervals = list()
    for i in range(m):
        s = input().strip().split()
        a, b = int(s[0]), int(s[1])
        intervals.append([a, b])
    intervals = sorted(intervals)

    stack = list() # 这个stack就存储的是对应这个val，第一个坐标比它小的值
    indexVal = 0 # 这个表示到第几个数字了
    indexZone = 0 # 这个表示区间取到哪个地方了

    while indexVal < n:
        val = points[indexVal][0]
        if indexVal == m and stack == []:
            break

        if indexZone < m and val >= intervals[indexZone][0]:
            while indexZone < m and val >= intervals[indexZone][0]:
                stack.append(intervals[indexZone])
                indexZone += 1
                
        num = 0
        stack.sort(key = lambda x: -x[1])
        curIndex = 0
        while curIndex < len(stack):
            if stack[curIndex][1] >= val:
                curIndex += 1
                num += 1
            curIndex += 1
        stack = stack[:curIndex] # 将不符合要求的全部删除

        points[indexVal][2] = num
        indexVal += 1

    # 如果提前结束，也即是indexVal != n - 1; 则表示后面的数全都为0，而且本来也不需要做修改
    print("Case #{}:".format(round + 1))
    points.sort(key = lambda x: x[1])
    for val in points:
        print(val[2])

