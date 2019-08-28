'''
@Descripttion: 算式转移
@Author: daxiong
@Date: 2019-08-27 19:44:58
@LastEditors: daxiong
@LastEditTime: 2019-08-28 09:38:18
'''
# n = int(input().strip())
# strL = input().strip()
n = 6
strL = "3 + 2 + 1 + -4 * -5 + 1"
strL = strL.split(' ')
number = [int(x) for x in strL if x != '+' and x != '-' and x != '*' and x != '/']
operators = [x for x in strL if x == '+' or x == '-' or x == '*' or x == '/']
begin = 0 # 这里记录的是符号
end =  n -1

while begin < n -1:
    if operators[begin] == '+':
        end = begin 
        while end < n - 1 and operators[end] == '+':
            end += 1
        a = begin
        if begin != 0:
            a = begin + 1
        b = end 
        if end != n - 1:
            b = end - 1
        temp = number[a: b + 1]
        temp.sort()
        for i in range(a, b + 1):
            number[i] = temp[i - a]
        begin = end
    elif operators[begin] == '*': # 乘法
        if number[begin] > number[begin + 1]:
            number[begin], number[begin + 1] = number[begin + 1], number[begin]
        begin += 1
    else:
        begin += 1

for i in range(0, 2*n, 2):
    operators.insert(i, str(number[int(i/2)]))

operators = ' '.join(operators)
print(operators) 

# 仅仅是把加法的值全都拿出来从小到大排序，然后对于乘法就将小的数放前面，然后对于减法和除不管。是不是这样？
# 最后生成的时候，我们符号的顺序是不会变的。