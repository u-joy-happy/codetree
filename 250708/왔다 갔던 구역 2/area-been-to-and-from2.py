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
        for j in range(cur+1, cur+x[i]+1) :
            if arr[j] < 2 :
                arr[j] += 1
        cur = cur + x[i]
    else :
        for j in range(cur-x[i], cur) :
            if arr[j] < 2 :
                arr[j] += 1
        cur = cur - x[i]

print(arr.count(2))