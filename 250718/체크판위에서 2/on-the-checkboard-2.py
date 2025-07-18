R, C = map(int, input().split())
grid = [list(input().split()) for _ in range(R)]

# Please write your code here.

goal = ''
if grid[0][0] == 'W':
    goal = 'B'
else :
    goal = 'W'
cnt = 0

if grid[-1][-1] == goal:
    for i in range(1, R-1):
        for j in range(1, C-1):
            if grid[i][j] == goal:
                goal = 'B' if goal == 'W' else 'W'
                for k in range(i+1, R-1):
                    for l in range(j+1, C-1):
                        if grid[k][l] == goal:
                            cnt += 1
                goal = 'B' if goal == 'W' else 'W'

print(cnt)