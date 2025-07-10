n = int(input())
x1, y1, x2, y2 = [], [], [], []
for _ in range(n):
    a, b, c, d = map(int, input().split())
    x1.append(a)
    y1.append(b)
    x2.append(c)
    y2.append(d)

# Please write your code here.

arr = [[0 for _ in range(200 + 1)] for _ in range(200 + 1)]

for i in range(n) :
    for y in range(y1[i], y2[i]):
        for x in range(x1[i], x2[i]):
            if i % 2 == 0 :
                arr[y][x] = 0
            else :
                arr[y][x] = 1

sum_val = 0
for item in arr :
    sum_val += sum(item)

print(sum_val)

