n = int(input())
commands = [tuple(input().split()) for _ in range(n)]
x = []
dir = []
for num, direction in commands:
    x.append(int(num))
    dir.append(direction)

# Please write your code here.

arr = [0] * 100 * n * 2

cur = (100 * n * 2) // 2

for i in range(n):
    if dir[i] == 'R' :
        for idx in range(cur, cur + x[i]):
            arr[idx] = abs(arr[idx]) + 1
    else :
        for idx in range(cur, cur - x[i], -1):
            arr[idx] = -(abs(arr[idx]) + 1)
    cur = idx

w_cnt = 0
b_cnt = 0
g_cnt = 0

for item in arr:
    if item == 0 :
        continue
    elif item <= -4 or item >= 4 :
        g_cnt += 1
    elif item < 0 :
        w_cnt += 1
    elif item > 0 :
        b_cnt += 1

print(w_cnt, b_cnt, g_cnt)
