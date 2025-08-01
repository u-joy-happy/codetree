N, B = map(int, input().split())
gifts = [tuple(map(int, input().split())) for _ in range(N)]
P = [gift[0] for gift in gifts]
S = [gift[1] for gift in gifts]

# Please write your code here.

max_val = 0

for i in range(N):
    arr = [0] * N
    for j in range(N):
        price = P[j]
        if i == j :
            price //= 2
        price += S[j]
        arr[j] = price
    arr.sort()

    tot, cnt = 0, 0
    for k in range(N):
        if tot + arr[k] <= B :
            tot += arr[k]
            cnt += 1
    max_val = max(max_val, cnt)

print(max_val)