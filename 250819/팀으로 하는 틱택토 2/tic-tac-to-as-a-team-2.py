inp = [input() for _ in range(3)]

# Please write your code here.

cnt = 0

def check(n, i, j):
    i, j = str(i), str(j)
    if n[0] == i and n[1] == i and n[2] == i :
        return False
    elif n[0] == j and n[1] == j and n[2] == j :
        return False
    elif (n[0] == i or n[0] == j) and (n[1] == i or n[1] == j) and (n[2] == i or n[2] == j) :
        return True
    return False

for i in range(1, 10) :
    for j in range(i + 1, 10) :
        
        flag = False 

        crs_str1 = ''
        for m in range(3) :
            nx, ny = 0 + (1 * m), 0 + (1 * m) 
            crs_str1 += inp[nx][ny]

        if check(crs_str1, i, j):
            flag = True
        
        crs_str2 = ''
        for m in range(3) :
            nx, ny = 0 + (1 * m), 2 + (-1 * m) 
            crs_str2 += inp[nx][ny]
            
        if check(crs_str2, i, j):
            flag = True
        
        for n in range(3):
            ver_str = ''
            for m in range(3):
                ver_str += inp[m][n]

            if check(inp[n], i, j) :
                flag = True

            if check(ver_str, i, j):
                flag = True
        
        if flag :
            cnt += 1

print(cnt)