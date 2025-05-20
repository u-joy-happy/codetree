a, b = map(int, input().split())

# Please write your code here.

def contain369(a) :
    flag = False
    for item in str(a) :
        if item == '3' or item == '6' or item == '9':
            flag = True
    return flag

def is_magic_number(a, b) :
    cnt = 0
    for i in range(a, b+1) :
        if i % 3 == 0 :
            cnt += 1
        elif contain369(i) :
            cnt += 1
    return cnt 

print(is_magic_number(a, b))