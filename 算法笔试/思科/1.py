'''
@Descripttion: 解析数据
@Author: daxiong
@Date: 2019-09-23 18:45:57
@LastEditors: daxiong
@LastEditTime: 2019-09-23 20:00:12
'''
s = input().strip()
tag = True
if s[-1] == '"':
    s = s[1: -1]
else:
    s = s[1: ]
    tag = False

s = s[::-1]
if tag == False:
    s = s[s.index('<') + 2: ]
else:
    s = s[s.index('<') + 1: ]
s = s[::-1]
if s[ :3] == "%22" and s[-3: ] == "%22":
    s = s[3: -3]
print(s)