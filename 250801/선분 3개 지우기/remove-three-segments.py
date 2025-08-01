n = int(input())
l = []
r = []
for _ in range(n):
    left, right = map(int, input().split())
    l.append(left)
    r.append(right)

# Please write your code here.

res = 0
for i in range(n) :
    for j in range(i+1, n) :
        arr = [0] * 101
        for x in range(l[i], r[i]+1):
            arr[x] += 1
        for x in range(l[j], r[j]+1):
            arr[x] += 1
        if max(arr) == 1 :
            res += 1

print(res)