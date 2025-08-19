N, K = map(int, input().split())
arr = [int(input()) for _ in range(N)]

# Please write your code here.

max_cnt = 0
for i in range(N):
    cnt = 0
    for j in range(N):
        if arr[i] <= arr[j] <= arr[i] + K :
            cnt += 1
    max_cnt = max(max_cnt, cnt)

print(max_cnt)