N, B = map(int, input().split())
P = [int(input()) for _ in range(N)]

# Please write your code here.

max_val = 0

P.sort()
for i in range(N):
    cnt, price = 0, 0
    for j in range(N):
        tmp = P[j]
        if i == j :
            tmp //= 2
        if price + tmp <= B :
            price += tmp
            cnt += 1
    max_val = max(max_val, cnt)
        
print(max_val)


