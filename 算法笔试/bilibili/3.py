s = input().strip().split()
N, S = int(s[0]), int(s[1])
arr = [int(i) for i in input().strip().split()]
if sum(arr) < S:
    print(-1)

begin = 0
end = 0
maxLen = N
sumNum = 0
while begin < N:
    if end == N:
        break
    while sumNum < S and end < N:
        sumNum += arr[end]
        end += 1
    if maxLen > end - begin:
        maxLen = end - begin
    while sumNum > S:
        begin += 1
        sumNum -= arr[begin]
    print(begin, end)
print(maxLen)