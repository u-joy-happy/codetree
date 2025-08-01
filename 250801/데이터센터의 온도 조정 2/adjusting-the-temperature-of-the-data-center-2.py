N, C, G, H = map(int, input().split())
ranges = [tuple(map(int, input().split())) for _ in range(N)]

# Please write your code here.

def check_temp(temp, t1, t2):
    global C, G, H
    if temp < t1 :
        return C
    elif t1 <= temp <= t2 :
        return G
    elif t2 < temp :
        return H

max_val = 0

for i in range(1001):
    tot = 0
    for j in range(N):
        tot += check_temp(i, ranges[j][0], ranges[j][1])
    max_val = max(max_val, tot)

print(max_val)