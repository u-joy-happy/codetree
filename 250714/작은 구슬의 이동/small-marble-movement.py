n, t = map(int, input().split())
r, c, d = input().split()
r, c = int(r), int(c)

# Please write your code here.

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

di = {'L':0, 'U':1, 'D':2, 'R':3}
dir_num = di[d]

y, x = r-1, c-1

def in_range(x, y) :
    global n
    return x >= 0 and x < n and y >= 0 and y < n

for i in range(t) :
    x, y = x + dx[dir_num], y + dy[dir_num]
    if not in_range(x, y) :
        dir_num = 3 - dir_num
        x, y = x + dx[dir_num], y + dy[dir_num]

print(y+1, x+1)
        