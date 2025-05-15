n, m = map(int, input().split())

# Please write your code here.

def euclidean(n, m):
    tmp = -1

    if n < m : 
        n, m = m, n

    while True :
        tmp = n % m
        if tmp == 0 :
            break 
        n = m
        m = tmp
    
    return m

print(euclidean(n,m))