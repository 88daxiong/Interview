'''
@Descripttion: 最大的雨水坑
@Author: daxiong
@Date: 2019-08-19 15:42:49
@LastEditors: daxiong
@LastEditTime: 2019-08-19 15:56:36
'''

def getMaxWater(array):
    left = 0
    right = len(array) - 1
    maxLeft = array[left]
    maxRight = array[right]
    maxWater = (min(maxLeft, maxRight) * (right - left))

    while left < right:
        if maxLeft <= maxRight:
            while left < right and array[left] <= maxLeft:
                left += 1
            if left == right:
                break
            else:
                maxLeft = array[left]
                if (min(maxLeft, maxRight) * (right - left)) > maxWater:
                    maxWater = (min(maxLeft, maxRight) * (right - left))
        else:
            while right > left and array[right] <= maxRight:
                right -= 1
            if left == right:
                break
            else:
                maxRight = array[right]
                if (min(maxLeft, maxRight) * (right - left)) > maxWater:
                    maxWater = (min(maxLeft, maxRight) * (right - left))
    return maxWater
            
array = [1, 9, 6, 2, 5, 4,  3, 10, 7]
print(getMaxWater(array))