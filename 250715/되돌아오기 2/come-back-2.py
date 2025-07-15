commands = input()

# Please write your code here.

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

dir_num = 0
x, y = 0, 0

res, time = 0, 0

for com in commands:
    if com == 'L' :
        dir_num = (dir_num + 4 - 1) % 4
    elif com == 'R' :
        dir_num = (dir_num + 1) % 4
    elif com == 'F' :
        x, y = x + dx[dir_num], y + dy[dir_num]
    time += 1

    if x == 0 and y == 0 :
        res = time
        break

print(res)