n, m = map(int, input().split())
arr = [[0] * m for _ in range(n)]

# Please write your code here.

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def in_range(x, y):
    global n, m
    return x >= 0 and x < m and y >= 0 and y < n

num = 1
x, y = 0, 0
dir_num = 0
for ny in range(n) :
    for nx in range(m) :
        if not ny and not nx :
            arr[y][x] = num
            num += 1
            continue
        else :     
            x, y = x + dx[dir_num], y + dy[dir_num]
        
        if not in_range(x,y) or arr[y][x] != 0 :
            x, y = x - dx[dir_num], y - dy[dir_num]
            dir_num = (dir_num + 1) % 4
            x, y = x + dx[dir_num], y + dy[dir_num]
        
        arr[y][x] = num
        num +=1

for ar in arr :
    for a in ar :
        print(a, end=' ')
    print() 