n = int(input())
grid = [[0] * n for _ in range(n)]

# Please write your code here.
center = int(n/2)
x, y = center, center
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]
dir_num = 0
val, cnt = 2, 1
grid[y][x] = 1

def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < n

flag = True
while flag:
    for _ in range(2):
        for i in range(cnt):
            nx, ny = x + dx[dir_num], y + dy[dir_num]
            if not in_range(nx, ny):
                flag = False
                break
            x, y = nx, ny
            grid[y][x] = val
            val += 1
        dir_num = (dir_num + 1) % 4
        if not flag:
            break
    cnt += 1

for item in grid:
    for it in item:
        print(it, end=' ')
    print()