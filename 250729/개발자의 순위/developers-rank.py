k, n = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(k)]

# Please write your code here.

res = 0

for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j :
            continue
        cnt = 0
        for l in range(k):
            idx1, idx2 = 0, 0 
            for idx, item in enumerate(arr[l]):
                if item == i : idx1 = idx
                elif item == j : idx2 = idx
            if idx1 < idx2 : cnt += 1
        if cnt == k :
            res += 1

print(res)
