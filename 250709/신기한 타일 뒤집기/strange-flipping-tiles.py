n = int(input())
commands = [tuple(input().split()) for _ in range(n)]
x = []
dir = []
for num, direction in commands:
    x.append(int(num))
    dir.append(direction)

# Please write your code here.

arr = [0 for _ in range(100 * n * 2 + 1)]

cur = (100 * n * 2) // 2

for i in range(n):
    if dir[i] == 'R' :
        for idx in range(cur, cur + x[i]):
            arr[idx] = 1
    else :
        for idx in range(cur, cur - x[i], -1):
            arr[idx] = 2
    cur = idx

w_cnt = 0
b_cnt = 0

for item in arr:
    if item == 0 :
        continue
    elif item == 1 :
        b_cnt += 1
    elif item == 2 :
        w_cnt += 1

print(w_cnt, b_cnt)