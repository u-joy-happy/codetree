a, b = map(int, input().split())

# Please write your code here.

def is_decimal(a) :
    for i in range(2, a):
        if a % i == 0 :
            return False
    return True

def sum_decimal(a, b) :
    sum_val = 0
    for i in range(a, b+1) :
        if is_decimal(i) :
            sum_val += i 
    return sum_val

print(sum_decimal(a, b))