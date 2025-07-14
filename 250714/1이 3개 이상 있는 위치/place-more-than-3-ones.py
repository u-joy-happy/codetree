n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

def in_range(x, y):
    global n
    return x >= 0 and y >= 0 and x < n and y < n  

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

tot = 0
for y in range(n):
    for x in range(n) :
        cnt = 0
        for i in range(4) :
            nx, ny = x + dx[i], y + dy[i]
            if in_range(nx, ny) and grid[ny][nx] == 1 :
                cnt += 1
        if cnt >= 3 :
            tot += 1

print(tot)