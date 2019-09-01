'''
@Descripttion: 消消乐
@Author: daxiong
@Date: 2019-09-01 20:00:21
@LastEditors: daxiong
@LastEditTime: 2019-09-01 20:22:49
'''
T = int(input().strip())

for i in range(T):
    n = int(input().strip())
    arr = input().strip().split()
    arr = [int(x) for x in arr]
    nums = list()
    for c in set(arr):
        nums.append(arr.count(c))
    nums.sort()
    while nums != [] and len(nums) != 1:
        nums[-2] -= 1
        nums[-1] -= 1
        if nums[-1] == 0:
            nums.pop(-1) # 这个时候最后两个肯定都为1
            nums.pop(-1)
        if len(nums) >= 2 and nums[-2] == 0:
            nums.pop(-2)
        nums.sort()
        
    if nums == []:
        print("YES")
    else:
        print("NO")
