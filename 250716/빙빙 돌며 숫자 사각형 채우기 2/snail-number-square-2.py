n, m = map(int, input().split())

# Please write your code here.

dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

arr = [[0] * m for _ in range(n)]
# cnt = 1
x, y = 0, 0
dir_num = 0
arr[0][0] = 1

def in_range(x, y):
    return x >= 0 and x < m and y >= 0 and y < n

for i in range(n*m-1) :
    nx, ny = x + dx[dir_num], y + dy[dir_num]
    if not in_range(nx, ny) or arr[ny][nx] != 0:
        dir_num = (dir_num + 1) % 4
        nx, ny = x + dx[dir_num], y + dy[dir_num]
    x, y = nx, ny
    arr[y][x] = i+2

for item in arr :
    for i in item:
        print(i, end=' ')
    print()

