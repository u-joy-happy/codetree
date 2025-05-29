n, m = map(int, input().split())
A = list(map(int, input().split()))

# Please write your code here.

def div_and_sum():
    global n, m
    tot = 0
    for _ in range(n) :
        tot += A[m-1]

        if m == 1 :
            break

        if m % 2 == 0 :
            m //= 2 
        else :
            m -= 1
        
    return tot

print(div_and_sum())