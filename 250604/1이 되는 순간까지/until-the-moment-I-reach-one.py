N = int(input())

# Please write your code here.

def div_cnt(n) :
    if n == 1 :
        return 0
    
    if n % 2 == 0 :
        return div_cnt(n//2) + 1
    else :
        return div_cnt(n//3) + 1

print(div_cnt(N))