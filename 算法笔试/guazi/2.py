'''
@Descripttion: 
@Author: daxiong
@Date: 2019-08-26 15:17:43
@LastEditors: daxiong
@LastEditTime: 2019-08-26 15:57:54
'''

strL = input().strip()
strL = [ord(x) for x in strL]
if max(strL) <= 90 and min(strL) >= 65: # 全部大写
    print("true")
elif strL[0] >= 65 and strL[0] <= 90  and max(strL[1:]) <= 122 and min(strL[1:]) >= 97: # 首字母大写
    print("true")
elif min(strL) >= 97 and min(strL) <= 122: # 全部小写
    print("true")
else:
    print("false")

# 一个简单的思路就是全部化成数字，然后看数字的范围即可。