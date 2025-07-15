N = int(input())
moves = [tuple(input().split()) for _ in range(N)]
dir = [move[0] for move in moves]
dist = [int(move[1]) for move in moves]

# Please write your code here.

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

di = {'W':0, 'N':1, 'E':2, 'S':3}

def get_return_time():
    res = -1
    time = 0
    x, y = 0, 0

    for i in range(N):
        dir_num = di[dir[i]]
        for _ in range(dist[i]):
            x, y = x + dx[dir_num], y + dy[dir_num]
            time += 1
            if x == 0 and y == 0:
                res = time
                return res
    return res

print(get_return_time())
