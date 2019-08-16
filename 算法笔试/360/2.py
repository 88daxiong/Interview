'''
@Description: In User Settings Edit
@Author: daxiong
@Date: 2019-08-15 18:44:38
@LastEditTime: 2019-08-16 10:52:18
@LastEditors: daxiong
'''
n = 5 
m = 5 
a = [0,2,4,1,1]
b = [1,1,1,0,0]

result = dict()
aDict = dict()
bDict = dict()

for c in set(a):
    aDict[c] = a.count(c)

for c in set(b):
    bDict[c] = b.count(c)

for akey in aDict.keys():
    for bkey in bDict.keys():
        value = (akey + bkey) % m
        if value not in result:
            result[value] = list()
        result[value].append( (akey,bkey) )
        
target = []

for i in range(m-1, -1, -1):
    if i in result:
        for tmp in result[i]:
            while tmp[0] in aDict and tmp[1] in bDict:
                target.append(i)
                aDict[tmp[0]] -=1 
                bDict[tmp[1]] -=1
                if aDict[tmp[0]] == 0:
                    aDict.pop(tmp[0])  
                if bDict[tmp[1]] == 0 :
                    bDict.pop(tmp[1])
print(target)  


# 主要的思想是把第一个数a里面的元素及其个数存储下来，第二个数b里面的元素及其个数存储下来。
# 然后遍历的保存aDict和bDict里面的元素求和模M之后的值，比如为c的话，将后续遍历的所有和模M等于c的值看作一个list保存。这个的复杂度是len(set(a))*len(set(b))，最多为M平方。
# 这样我们就得到了两个数想加的所有和，以及原始值。
# 接下来就从最大的值开始遍历，比如是m-1，然后就找出m-1这个里面在a和b里面的元素分别是什么，在aDict和bDict里面依次减去，直到为0;
# 遍历完结果也就出来了。