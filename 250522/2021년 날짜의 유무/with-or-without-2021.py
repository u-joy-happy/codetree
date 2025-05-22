M, D = map(int, input().split())

# Please write your code here.

def is_valid(m, d) :
    if m > 12 or d > 31 :
        return False
    
    if m == 2 and d > 28 :
        return False
    
    if m <= 7 :
        if m % 2 == 1 and d > 31 :
            return False
        if m % 2 == 0 and d > 30 :
            return False
    else :
        if m % 2 == 0 and d > 31 :
            return False
        if m % 2 == 1 and d > 30 :
            return False
            
    return True
    
if is_valid(M, D) :
    print('Yes')
else :
    print('No')