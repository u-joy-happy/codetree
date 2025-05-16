n, m = map(int, input().split())

# Please write your code here.

def gcd(n, m):
    tmp = -1
    while True :
        tmp = n % m 
        if tmp == 0 :
            break
        n = m
        m = tmp 
    return m

def lcm(n, m) :
    gcd_val = gcd(n, m)
    return n * m // gcd_val

print(lcm(n, m))