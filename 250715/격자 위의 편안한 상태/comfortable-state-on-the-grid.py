n, m = map(int, input().split())
points = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.

dx, dy = [0, 0, -1, 1], [-1, 1, 0 ,0]

arr = [[0] * n for _ in range(n)]

def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < n

for i in range(m) :
    x, y = points[i]
    x, y = x-1, y-1
    flag = 0
    cnt = 0
    arr[x][y] = 1
    for di in range(4):
        nx, ny = x + dx[di], y + dy[di]
        if in_range(nx, ny) and arr[nx][ny] == 1 :
            cnt += 1
    if cnt == 3 :
        flag = 1
    print(flag)
