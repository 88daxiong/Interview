'''
@Descripttion: 算式转移
@Author: daxiong
@Date: 2019-08-28 09:37:28
@LastEditors: daxiong
@LastEditTime: 2019-08-28 13:14:19
'''
# n=int(input())
# s=list(input().split(" "))
s = "3 + 2 + 1 + -4 * -5 * -9 / 4 / 3 / 2 + 1 - 3 -1 -2"
s = s.split()
for i in range(len(s)):
    if s[i] in ['+','-','*','/']:
        new_s=s[:]
        for j in range(i,0,-2): # 从i这个符号往后遍历，更新
            if int(new_s[j + 1])>int(new_s[j - 1]): # 如果这个满足字典序，就直接返回
                break
            new_s[j + 1], new_s[j - 1] = new_s[j - 1], new_s[j + 1] # 如果前一个数比较大，就交换前后的数
            if eval("".join(new_s))==eval("".join(s)): # eval是用来计算表达式的值的，如果这两个值相同，就表示可以交换
                s=new_s[:]
            else:
                break # 如果不能交换，则s的值不变，直接继续遍历
print(" ".join(s))