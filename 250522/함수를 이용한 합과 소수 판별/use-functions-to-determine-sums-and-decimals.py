a, b = map(int, input().split())

# Please write your code here.

def is_decimal(a):
    if a == 1 :
        return False

    for i in range(2, a) :
        if a % i == 0 :
            return False
    return True

def sum_digit(a) :
    return ((a // 10) + (a % 10)) % 2 == 0

cnt = 0

for i in range(a, b+1) :
    if is_decimal(i) and sum_digit(i) :
        cnt += 1

print(cnt)