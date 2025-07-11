dirs = input()

# Please write your code here.

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

x, y = 0, 0
idx = 0

for d in dirs :
    if d == 'L' :
        idx = (idx + 4 - 1) % 4
    elif d == 'R' :
        idx = (idx + 1) % 4
    elif d == 'F' :
        x += dx[idx]
        y += dy[idx]

print(x, y)