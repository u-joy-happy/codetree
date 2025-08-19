N = int(input())
seat = list( input())

# Please write your code here.

max_val = 0

def min_dist() :
    dist = N
    for i in range(N):
        for j in range(i+1, N):
            if seat[i] == '1' and seat[j] == '1':
                dist = min(dist, j - i)
    return dist

for i in range(N):
    if seat[i] == '0':
        seat[i] = '1'
        max_val = max(max_val, min_dist())
        seat[i] = '0'

print(max_val)