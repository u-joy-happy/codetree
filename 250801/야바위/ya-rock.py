n = int(input())
moves = [tuple(map(int, input().split())) for _ in range(n)]
a, b, c = zip(*moves)
a, b, c = list(a), list(b), list(c)

# Please write your code here.

max_val = 0
res = -1
for x in range(1, 4):
    tot = 0
    arr = [0] * 4
    arr[x] = 1
    for i in range(n):
        arr[a[i]], arr[b[i]] = arr[b[i]], arr[a[i]]
        if arr[c[i]] == 1:
            tot += 1
    if tot >= max_val:
        max_val = tot
        res = x 

print(res)