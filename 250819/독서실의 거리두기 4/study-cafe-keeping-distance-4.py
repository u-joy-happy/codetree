N = int(input())
seat = list(input())

# Please write your code here.

max_dist = 0

def min_dist():
    dist = N
    for x in range(N):
        for y in range(x+1, N):
            if seat[x] == '1' and seat[y] == '1' :
                dist = min(dist, y - x)
    return dist

for i in range(N):
    for j in range(i+1, N):
        if seat[i] != '1' and seat[j] != '1' :
            seat[i], seat[j] = '1', '1'
            max_dist = max(max_dist, min_dist())
            seat[i], seat[j] = '0', '0'

print(max_dist)