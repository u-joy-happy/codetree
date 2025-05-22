a, b = map(int, input().split())

# Please write your code here.

def is_decimal(a):
    for i in range(2, a) :
        if a % i == 0 :
            return False
    return True

def sum_digit(a) :
    if a // 10 == 0 :
        return a % 2 == 0
    else :
        return ((a // 10) + (a % 10)) % 2 == 0

cnt = 0

for i in range(a, b+1) :
    if i == 1 :
        continue
    elif is_decimal(i) and sum_digit(i) :
        cnt += 1

print(cnt)