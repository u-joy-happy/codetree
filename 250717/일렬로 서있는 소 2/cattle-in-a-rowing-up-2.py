N = int(input())
A = list(map(int, input().split()))

# Please write your code here.

cnt, res = 0, 0
max_val = 0

for i in range(N):
    for j in range(i, N):
        if A[j] > max_val:
            max_val = A[j]
            cnt += 1
    if cnt >= 3 :
        res += 1
    cnt, max_val = 0, 0

print(res)