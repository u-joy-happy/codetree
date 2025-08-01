n = int(input())
l = []
r = []
for _ in range(n):
    left, right = map(int, input().split())
    l.append(left)
    r.append(right)

# Please write your code here.

res = 0
arr = [0] * 101

for i in range(n) :
    for x in range(l[i], r[i]+1):
        arr[x] += 1

for i in range(n) :
    for j in range(i+1, n) :
        for k in range(j+1, n) :
            tmp_arr = arr * 1
            for x in range(l[i], r[i]+1):
                tmp_arr[x] -= 1
            for x in range(l[j], r[j]+1):
                tmp_arr[x] -= 1
            for x in range(l[k], r[k]+1):
                tmp_arr[x] -= 1
            if max(tmp_arr) <= 1 :
                res += 1

print(res)