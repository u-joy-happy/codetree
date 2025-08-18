inp = [input() for _ in range(3)]

# Please write your code here.

dx, dy = [1, 1], [1, -1]

cnt = 0
flag = True 

def check(n, i, j):
    i, j = str(i), str(j)
    if n[0] == i and n[1] == i and n[2] == i :
        return False
    elif n[0] == j and n[1] == j and n[2] == j :
        return False
    elif (n[0] == i or n[0] == j) and (n[1] == i or n[1] == j) and (n[2] == i or n[2] == j) :
        return True

for i in range(1, 10) :
    for j in range(i + 1, 10) :

        crs_str1 = ''
        for m in range(3) :
            nx, ny = 0 + (dx[0] * m), 0 + (dy[0] * m) 
            crs_str1 += inp[nx][ny]
        
        crs_str2 = ''
        for m in range(3) :
            nx, ny = 0 + (dx[1] * m), 2 + (dy[1] * m) 
            crs_str2 += inp[nx][ny]
        
        for n in range(3):
            ver_str = ''
            for m in range(3):
                ver_str += inp[m][n]

            if check(inp[n], i, j) :
                flag = True
                break
            else :
                flag = False

            if check(ver_str, i, j):
                flag = True
                break
            else :
                flag = False

            if check(crs_str1, i, j):
                flag = True
                break
            else :
                flag = False
                
            if check(crs_str2, i, j):
                flag = True
                break
            else :
                flag = False
        
        if flag :
            cnt += 1
            break 

print(cnt)