x1 = [0] * 3
y1 = [0] * 3
x2 = [0] * 3
y2 = [0] * 3

x1[0], y1[0], x2[0], y2[0] = map(int, input().split())
x1[1], y1[1], x2[1], y2[1] = map(int, input().split())
x1[2], y1[2], x2[2], y2[2] = map(int, input().split())

# Please write your code here.

arr = [[0 for _ in range(2 * 1000 + 1)] for _ in range(2 * 1000 + 1)]

for i in range(3):
    for y in range(y1[i], y2[i]):
        for x in range(x1[i], x2[i]):
            if i == 2 :
                arr[y][x] = 0
            else :
                arr[y][x] = 1

sum_val = 0
for item in arr :
    sum_val += sum(item)

print(sum_val)
