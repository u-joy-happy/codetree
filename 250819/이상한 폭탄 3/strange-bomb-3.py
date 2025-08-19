N, K = map(int, input().split())
num = [int(input()) for _ in range(N)]

# Please write your code here.

def check(arr):
    max_idx, max_cnt = 0, 0
    idx = 0
    for x in range(len(arr)):
        cnt = 0
        for y in range(x, len(arr)):
            if arr[x] == arr[y] :
                cnt += 1
                idx = arr[x]
        if cnt >= max_cnt :
            max_cnt = cnt
            max_idx = idx
    return max_idx, max_cnt

tmp = 0
res = 0

for i in range(N-K):
    idx, cnt = check(num[i:i+K+1])
    if cnt >= tmp :
        tmp = cnt
        res = idx
    if cnt == tmp :
        res = max(idx, res)

print(res)