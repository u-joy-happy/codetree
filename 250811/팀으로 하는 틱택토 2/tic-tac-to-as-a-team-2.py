inp = [input() for _ in range(3)]

# Please write your code here.

def check(arr):
    return len(set(arr)) == 2
    
dx, dy = [0, 1, 1, 1], [1, 0, 1, -1]

cnt = 0
for i in range(3):
    for j in range(3):
        dir = []
        if j == 0 :
            dir.append(0)
        if i == 0 :
            dir.append(1)
        if i == 0 and j == 0 :
            dir.append(2)
        if i == 0 and j == 2 :
            dir.append(3)
        
        for d in dir :
            val = []
            for k in range(3):
                nx, ny = i + dx[d] * k, j + dy[d] * k
                val.append(inp[nx][ny])
            if check(val) :
                cnt += 1
print(cnt)