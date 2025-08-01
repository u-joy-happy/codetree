T, a, b = map(int, input().split())
c = []
x = []
for _ in range(T):
    char, pos = input().split()
    c.append(char)
    x.append(int(pos))

# Please write your code here.

res = 0

for i in range(a, b+1):
    S_dist, N_dist = 1000, 1000
    for j in range(T):
        dist = abs(i - x[j])
        if c[j] == 'S' :
            S_dist = min(dist, S_dist)
        else :
            N_dist = min(dist, N_dist)
    if S_dist <= N_dist :
        res += 1

print(res)
            
