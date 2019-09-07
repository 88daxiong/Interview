'''
@Descripttion: Mars Numbers
@Author: daxiong
@Date: 2019-09-06 16:02:25
@LastEditors: daxiong
@LastEditTime: 2019-09-06 16:36:47
'''
dicEearth2MarsA = dict() # 保存个位转换 地球文字转换火星文字
dicEearth2MarsB = dict() # 保存十位转换 地球文字转换火星文字
dicMars2EearthA = dict() # 保存个位转换 火星文字转换地球文字
dicMars2EearthB = dict() # 保存个位转换 火星文字转换地球文字
arr1 = "tret, jan, feb, mar, apr, may, jun, jly, aug, sep, oct, nov, dec"
arr1 = arr1.split(',')
arr2 = "tam, hel, maa, huh, tou, kes, hei, elo, syy, lok, mer, jou"
arr2 = arr2.split(',')
for i in range(13):
    dicEearth2MarsA[str(i)] = arr1[i].strip()
for i in range(1, 13):
    dicEearth2MarsB[str(i)] = arr2[i - 1].strip()
for i in range(13):
    dicMars2EearthA[arr1[i].strip] = i
for i in range(1, 13):
    dicMars2EearthB[arr2[i - 1].strip] = i

N = int(input().strip())
for i in range(N):
    s = input().strip()
    try:
        a = int(s)
        if a > 12:
            b = a % 13 # 个位转换
            a = int(a / 13) # 十位转换
            print("{0} {1}".format(dicEearth2MarsB[str(a)], dicEearth2MarsA[str(b)]))
        else:
            print(dicEearth2MarsA(str(a)))
    except:
        s = s.split()
        if len(s) == 1:
            print(dicMars2EearthA[s[0]])
        else:
            print(dicMars2EearthB[s[1]] * 13 + dicMars2EearthA[s[0]])


