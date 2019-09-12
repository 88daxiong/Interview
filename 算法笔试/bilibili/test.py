'''
@Descripttion: 
@Author: daxiong
@Date: 2019-09-10 18:57:41
@LastEditors: daxiong
@LastEditTime: 2019-09-11 20:24:46
'''
def maxProfit(prices):
    n = len(prices)
    if n < 2:
        return 0
    dp1 = [0 for _ in range(n)]
    dp2 = [0 for _ in range(n)]
    minval = prices[0]
    maxval = prices[-1]
    for i in range(1,n):
        dp1[i] = max(dp1[i-1], prices[i] - minval)
        minval = min(minval, prices[i])
    for i in range(n-2,-1,-1):
        dp2[i] = max(dp2[i+1], maxval - prices[i])
        maxval = max(maxval, prices[i])
    
    dp = [dp1[i] + dp2[i] for i in range(n)]
    return max(dp)

x = [int(x) for x in input().strip().split(' ')]
print(maxProfit(x))