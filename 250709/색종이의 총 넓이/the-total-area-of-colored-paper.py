n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x, y = zip(*points)
x, y = list(x), list(y)

# Please write your code here.

arr = [[0 for _ in range(100 * 2 + 1)] for _ in range(100 * 2 + 1)]
OFFSET = 100

for i in range(n) :
    for y_axis in range(y[i], y[i]+8) :
        for x_axis in range(x[i], x[i]+8) :
            arr[y_axis+OFFSET][x_axis+OFFSET] = 1


sum_val = 0
for item in arr :
    sum_val += sum(item)

print(sum_val)

