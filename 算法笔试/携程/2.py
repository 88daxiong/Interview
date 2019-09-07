'''
@Descripttion: AUC计算
@Author: daxiong
@Date: 2019-09-04 19:58:23
@LastEditors: daxiong
@LastEditTime: 2019-09-04 20:09:16
'''
N = int(input().strip())
prob = list()
labels = list()

for i in range(N):
    s = input().strip().split()
    labels.append(int(s[0]))
    prob.append(float(s[1]))

combine = list(zip(prob, labels))
rank = [x2 for x1, x2 in sorted(combine, key=lambda x: x[0])]
rankList = [i + 1 for i in range(len(rank)) if rank[i] == 1]
posNum = 0
negNum = 0
for i in range(len(labels)):
    if labels[i] == 1:
        posNum += 1
    else:
        negNum += 1
auc = (sum(rankList) - (posNum * (posNum + 1)) / 2) / (posNum * negNum)
print(auc)
