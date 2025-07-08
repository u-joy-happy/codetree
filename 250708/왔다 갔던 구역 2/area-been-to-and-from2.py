n = int(input())
x = []
dir = []
for _ in range(n):
    xi, di = input().split()
    x.append(int(xi))
    dir.append(di)

# Please write your code here.

arr = [0] * (100 * 10 * 2)

cur = 1000

for i in range(n):
    if dir[i] == 'R' :
        for j in range(cur, cur+x[i]) :
            arr[j] += 1
        cur = cur + x[i]
    else :
        for j in range(cur-x[i], cur) :
            arr[j] += 1
        cur = cur - x[i]

cnt = 0
for item in arr:
    if item >= 2 :
        cnt += 1

print(cnt)