n = int(input())
grid = [list(input()) for _ in range(n)]
k = int(input())

# Please write your code here.

#  N, E, W, S
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

dir_num = (k-1) // 3 
dir_seq = (k-1) % 3

def move(x, y, dir_num):
    if dir_num % 2 == 0 :
        if grid[x][y] == '/' :
            dir_num = (dir_num + 4 - 1) % 4
        else :
            dir_num = (dir_num + 1) % 4
    else :
        if grid[x][y] == '/' :
            dir_num = (dir_num + 1) % 4
        else :
            dir_num = (dir_num + 4 - 1) % 4
    return x + dx[dir_num], y + dy[dir_num]

def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < n

def laser(x, y):
    if not in_range(x, y):
        return 0
    nx, ny = move(x, y, dir_num)
    return laser(nx, ny) + 1

print(laser(dir_num, dir_seq))
