n = int(input())
lines = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.

res = 0
for i in range(n):
    cnt = 0
    for j in range(n):
        x1, x2 = lines[i]
        x11, x22 = lines[j]
        if x1 < x11 and x2 > x22 or x1 > x11 and x2 < x22 :
            cnt = 0
            break
        cnt = 1
    res += cnt 
print(res)