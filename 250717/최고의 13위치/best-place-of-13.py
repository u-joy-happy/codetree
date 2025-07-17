n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

res = 0

for i in range(n):
    for j in range(n-2):
        val = sum(grid[i][j:j+3])
        if val > res :
            res = val

print(res)