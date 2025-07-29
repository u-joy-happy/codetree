N, K = map(int, input().split())
num = [int(input()) for _ in range(N)]

# Please write your code here.
max_val = -1
for i in range(N):
    for j in range(i, N):
        if i == j :
            continue
        if abs(i - j) <= K and num[i] == num[j] :
            max_val = max(max_val, num[i])

print(max_val)