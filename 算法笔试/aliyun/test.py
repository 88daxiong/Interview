'''
@Description: In User Settings Edit
@Author: your name
@Date: 2019-08-12 22:10:42
@LastEditTime: 2019-08-14 11:33:33
@LastEditors: Please set LastEditors
'''

def convert(n, decimal):
    num = list()
    while n:
        num.append(n % decimal)
        n = int(n / decimal)
    return sum(num)

result = 0
for i in range(2, 3):
    result += convert(3, i)
print(result)