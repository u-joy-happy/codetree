board = [list(map(int, input().split())) for _ in range(19)]

# Please write your code here.

dx = [0, 0, 1, -1, 1, -1, -1, 1]
dy = [1, -1, 0, 0, 1, -1, 1, -1]

x, y = 0, 0
res = 0

def check(i, j, color):
    global x, y
    for n in range(8):
        nx, ny = i + dx[n], j + dy[n]
        if color == board[nx][ny] :
            for m in range(5):
                nx, ny = i + dx[n] * m, j + dy[n] * m
                if color != board[nx][ny]:
                    return False
            x, y = (i + nx) // 2, (j + ny) // 2
            return True
    return False

for i in range(19):
    for j in range(19):
        if board[i][j] != 0 :
            color = board[i][j]
            if check(i, j, color):
                res = color

print(res)
if res :
    print(x+1, y+1)