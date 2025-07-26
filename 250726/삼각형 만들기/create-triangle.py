n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]

# Please write your code here.

max_val = 0

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if x[i] != x[j] and x[j] != x[k] and x[i] != x[k] :
                continue
            if y[i] != y[j] and y[j] != y[k] and y[i] != y[k] :
                continue
            if x[i] == x[j] == x[k] or y[i] == y[j] == y[k] :
                continue
            min_x, min_y = min(x[i], x[j], x[k]), min(y[i], y[j], y[k])
            max_x, max_y = max(x[i], x[j], x[k]), max(y[i], y[j], y[k])
            ext = (max_x - min_x) * (max_y - min_y)
            max_val = max(max_val, ext)

print(max_val)