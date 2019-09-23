'''
@Descripttion: 计数V2.0
@Author: daxiong
@Date: 2019-09-20 20:17:18
@LastEditors: daxiong
@LastEditTime: 2019-09-20 20:20:27
'''
T = int(input().strip())

for round in range(T):
    s = input().strip().split()
    n, m = int(s[0]), int(s[1])
    points = [int(val) for val in input().strip().split()]
    intervals = list()
    for i in range(m):
        s = input().strip().split()
        a, b = int(s[0]), int(s[1])
        intervals.append([a, b])
    intervals = sorted(intervals)

    resNum = list()

    for val in points:
        indexZone = 0 # 这个表示区间取到哪个地方了
        num = 0
        if indexZone < m and val >= intervals[indexZone][0]:
            while indexZone < m and val >= intervals[indexZone][0]:
                if intervals[indexZone][1] >= val:
                    num += 1
                indexZone += 1
        resNum.append(num)

    # 如果提前结束，也即是indexVal != n - 1; 则表示后面的数全都为0，而且本来也不需要做修改
    print("Case #{}:".format(round + 1))
    for val in resNum:
        print(val)
