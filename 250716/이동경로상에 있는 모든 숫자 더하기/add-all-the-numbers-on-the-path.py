N, T = map(int, input().split())
str = input()
board = [list(map(int, input().split())) for _ in range(N)]

# Please write your code here.

dx, dy = [0, 1, 0, -1], [-1, 0, 1, 0]
x, y = N // 2, N // 2
dir_num = 0
sum_val = board[y][x]

def in_range(x, y):
    return x >= 0 and x < N and y >= 0 and y < N

for i in range(T):
    if str[i] == 'L' :
        dir_num = (dir_num + 4 - 1) % 4
    elif str[i] == 'R' :
        dir_num = (dir_num + 1) % 4
    elif str[i] == 'F' :
        x, y = x + dx[dir_num], y + dy[dir_num]
        if in_range(x, y):
            sum_val += board[y][x]
        else :
            x, y = x - dx[dir_num], y - dy[dir_num]

print(sum_val)