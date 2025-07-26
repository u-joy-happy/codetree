n = int(input())
times = [tuple(map(int, input().split())) for _ in range(n)]
a = [t[0] for t in times]
b = [t[1] for t in times]

# Please write your code here.
max_val = 0

for i in range(n) :
    arr = [0] * 1001
    for j in range(n) :
        if i == j :
            continue
        for x in range(a[j], b[j]):
            arr[x] = 1
    max_val = max(max_val, sum(arr))

print(max_val)