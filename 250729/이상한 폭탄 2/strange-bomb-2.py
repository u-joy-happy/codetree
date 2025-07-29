N, K = map(int, input().split())
num = [int(input()) for _ in range(N)]

# Please write your code here.
max_val = -1
for i in range(N-K):
    for j in range(i+1, i+K+1):
        if num[i] == num[j] :
            max_val = max(max_val, num[i])

print(max_val)