n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x, y = zip(*points)
x, y = list(x), list(y)

# Please write your code here.

flag = False
for i in range(11):
    for j in range(11):
        for k in range(11):
            for l in range(n):
                if x[l] == i or x[l] == j or x[l] == k and y[l] == i or y[l] == j or y[l] == k :
                    flag = True
print(1 if flag else 0)



