'''
@Descripttion: 
@Author: daxiong
@Date: 2019-09-09 19:19:52
@LastEditors: daxiong
@LastEditTime: 2019-09-10 09:51:57
'''
k = int(input().strip())
s = [x for x in input().strip()]

maxLen = 0
begin = 0
end = 0
curDic = dict()

while end < len(s):
    while len(curDic) <= k and end < len(s):
        if len(curDic) == k and s[end] not in curDic:
            break
        if s[end] not in curDic:
            curDic[s[end]] = 0
        curDic[s[end]] += 1
        end += 1
    if end - begin > maxLen:
        maxLen = end - begin
    while len(curDic) == k:
        curDic[s[begin]] -= 1
        if curDic[s[begin]] == 0:
            del curDic[s[begin]]
        begin += 1

print(maxLen)