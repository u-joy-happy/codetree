N, M = map(int, input().split())
arr = [input() for _ in range(N)]

# Please write your code here.

dx, dy = [-1, -1, -1, 0, 0, 1, 1, 1], [-1, 0, 1, -1, 1, -1, 0, 1]
res = 0

def in_range(x, y):
    return 0 <= x < N and 0 <= y < M

for i in range(N):
    for j in range(M):
        if arr[i][j] != 'L':
            continue
        for k in range(8):
            if in_range(i+dx[k], j+dy[k]) and arr[i+dx[k]][j+dy[k]] == 'E' \
               and in_range(i+dx[k]*2, j+dy[k]*2) and arr[i+dx[k]*2][j+dy[k]*2] == 'E':
                res += 1

print(res)