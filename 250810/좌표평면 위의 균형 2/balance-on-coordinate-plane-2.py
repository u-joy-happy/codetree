n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.

min_val = 100
for px in range(1, 101):
    for py in range(1, 101):
        v1, v2, v3, v4 = 0, 0, 0, 0
        for x, y in points :
            if x <= px and y <= py :
                v1 += 1
            elif x <= px and y > py :
                v2 += 1
            elif x > px and y <= py :
                v3 += 1
            elif x > px and y > py :
                v4 += 1
        max_val = max(v1, v2, v3, v4)
        min_val = min(min_val, max_val)
print(min_val)


