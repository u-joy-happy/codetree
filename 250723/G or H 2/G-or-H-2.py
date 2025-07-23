n = int(input())
people = [tuple(input().split()) for _ in range(n)]
pos = [int(p[0]) for p in people]
alpha = [p[1] for p in people]

# Please write your code here.

max_val = 0
arr = [0] * (max(pos)+1)
for i in range(n):
    arr[pos[i]] = alpha[i]

for i in range(len(arr)):
    if arr[i] == 0 : continue
    for j in range(len(arr)-1, i-1, -1):
        if arr[j] == 0 : continue
        g_cnt, h_cnt = 0, 0
        for k in range(i, j+1):
            if arr[k] == 'G' : g_cnt += 1
            elif arr[k] == 'H' : h_cnt += 1
        if g_cnt == h_cnt :
            max_val = max(max_val, j-i)

print(max_val)