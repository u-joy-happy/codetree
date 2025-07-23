N, K = map(int, input().split())
candy = []
pos = []

for _ in range(N):
    c, p = map(int, input().split())
    candy.append(c)
    pos.append(p)

# Please write your code here.

max_val = 0

for i in range(max(pos)):
    sum_val = 0
    for j in range(N):
        if i-K <= pos[j] <= i+K and 0 <= j <= 100 :
            sum_val += candy[j]
    max_val = max(max_val, sum_val)

print(max_val)
        
