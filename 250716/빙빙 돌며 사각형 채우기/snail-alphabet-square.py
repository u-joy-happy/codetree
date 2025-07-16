n, m = map(int, input().split())

# Please write your code here.

arr = [[''] * m for _ in range(n)]
dx, dy = [1, 0 , -1 ,0], [0, 1, 0, -1]

arr[0][0] = 'A'
x, y = 0, 0
dir_num = 0
a = 'A'

def check_alp():
    global a
    if ord(a) > ord('Z') :
        a = 'A'

def in_range(x, y):
    return x >= 0 and x < m and y >= 0 and y < n

for i in range(n*m-1) :
    a = chr(ord(a) + 1)
    check_alp()

    nx, ny = x + dx[dir_num], y + dy[dir_num]
    if not in_range(nx, ny) or arr[ny][nx] != '' :
        dir_num = (dir_num + 1) % 4
        nx, ny = x + dx[dir_num], y + dy[dir_num]
    x, y = nx, ny
    arr[y][x] = a

for item in arr:
    for it in item:
        print(it, end=' ')
    print()
