'''
@Descripttion: 
@Author: daxiong
@Date: 2019-08-26 15:02:28
@LastEditors: daxiong
@LastEditTime: 2019-08-26 15:53:48
'''
import sys
n = int(sys.stdin.readline().strip())
res = list(map(int,(input().strip().split(" "))))
if sorted(res, reverse = True) == res:
    print(0)
else:
    maxLen = 0
    for begin in range(0, n - maxLen):
        end = n - 1
        while begin < end - maxLen:
            if res[begin] > res[end]:
                end -= 1
            else:
                break
        if end - begin > maxLen:
            maxLen = end - begin
        
    print(maxLen)

# 双指针即可。从第一个元素开始遍历，然后从最后的一个开始往前数，找到第一个比它大的，然后比较与maxLen谁大即可。一个小的优化办法是直接在第一个遍历的时候，比较其索引与maxLen的和是否大于数组长度，如果大于就不需要再继续往下了。
        