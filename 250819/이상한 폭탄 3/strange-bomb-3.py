N, K = map(int, input().split())
num = [int(input()) for _ in range(N)]

# Please write your code here.

max_cnt = 0
max_idx = 0

for i in range(N-K):
    arr = num[i:i+K+1]
    idx = 0
    for x in range(len(arr)):
        cnt = 0
        for y in range(x, len(arr)):
            if arr[x] == arr[y] :
                cnt += 1
                idx = arr[x]
        if cnt > max_cnt : 
            max_cnt = cnt
            max_idx = idx
        elif cnt == max_cnt and idx > max_idx :
            max_idx = idx 

print(max_idx)