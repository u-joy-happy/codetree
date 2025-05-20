a, b = map(int, input().split())

# Please write your code here.

def is_magic_number(a, b) :
    cnt = 0
    for i in range(a, b+1) :
        if i % 3 == 0 :
            cnt += 1
        elif i % 10 in [3, 6, 9] :
            cnt += 1
        elif i // 10 in [3, 6, 9] :
            cnt += 1
    
    return cnt 

print(is_magic_number(a, b))