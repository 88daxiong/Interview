'''
@Descripttion: 
@Author: daxiong
@Date: 2019-08-29 19:53:13
@LastEditors: daxiong
@LastEditTime: 2019-08-29 20:26:40
'''
size = int(input().strip())
nums = input().split()
nums = [int(x) for x in nums]

tail = [nums[0]]

for i in range(1, size):
    left = 0
    right = len(tail)
    while left < right:
        mid = (left + right) >> 1

        if tail[mid] < nums[i]:
            left = mid + 1
        else:
            right = mid
    if left == len(tail):
        tail.append(nums[i])
    else:
        tail[left] = nums[i]
print(len(tail))




