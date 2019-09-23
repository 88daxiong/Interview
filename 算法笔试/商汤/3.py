'''
@Descripttion: 重复词
@Author: daxiong
@Date: 2019-09-21 19:11:47
@LastEditors: daxiong
@LastEditTime: 2019-09-21 20:30:44
'''
class Periods:
    def getLongest(self, n, s):
        # write code here
        resNum = 0
        tag = -1
        for i in range(n-1, 0, -1):
            if i > tag and tag > 0:
                resNum += tag
                continue
            if tag == 0:
                break
            tag = self.isRepeat(s[:i+1])
            resNum += tag
        return resNum
        
    def isRepeat(self, s):
        n = len(s) - 1
        for j in range(n, 0, -1):
            Q = s[:j] + s[:j]
            if Q[:len(s)] == s:
                return j
        return 0
        
x = Periods()
print(x.getLongest(8, 'babababa'))