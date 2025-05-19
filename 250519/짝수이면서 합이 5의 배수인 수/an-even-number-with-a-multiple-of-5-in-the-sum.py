n = int(input())

# Please write your code here.

def is_magic_number(n) :
    return n % 2 == 0 and ((n % 10) + (n // 10)) % 5 == 0 

if is_magic_number(n) :
    print('Yes')
else :
    print('No')