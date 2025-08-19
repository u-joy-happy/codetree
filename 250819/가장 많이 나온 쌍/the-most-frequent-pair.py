n, m = map(int, input().split())
pairs = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.

max_val = 0

for i in range(m) :
    cnt = 0
    for j in range(i, m):
        if (pairs[i][0] == pairs[j][0] and pairs[i][1] == pairs[j][1]) \
        or (pairs[i][0] == pairs[j][1] and pairs[i][1] == pairs[j][0]):
            cnt += 1
    max_val = max(max_val, cnt)

print(max_val)