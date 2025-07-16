n = int(input())
grid = [list(input()) for _ in range(n)]
k = int(input())

# Please write your code here.

dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]

dir_num = (k-1) // n
dir_seq = (k-1) % n

def get_start_point():
    x, y = 0, 0
    if dir_num == 0:
        x, y = 0, dir_seq
    elif dir_num == 1:
        x, y = dir_seq, 0
    elif dir_num == 2:
        x, y = n-1, (n-1)-dir_seq
    elif dir_num == 3:
        x, y = (n-1)-dir_seq, n-1
    return x, y 

def move(x, y):
    global dir_num
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
    nx, ny = move(x, y)
    return laser(nx, ny) + 1

x, y = get_start_point()
print(laser(x, y))