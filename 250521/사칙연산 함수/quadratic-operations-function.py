a, o, c = input().split()
a = int(a)
c = int(c)

# Please write your code here.

def get_sum(a, c) :
    return a + c

def get_diff(a, c) :
    return a - c

def get_div(a, c) :
    return a // c

def get_mult(a, c) :
    return a * c


if o == '+' :
    print(f'{a} + {c} = {get_sum(a, c)}')
elif o == '-' :
    print(f'{a} - {c} = {get_diff(a, c)}')
elif o == '/' :
    print(f'{a} / {c} = {get_div(a, c)}')
elif o == '*' :
    print(f'{a} * {c} = {get_mult(a, c)}')
else :
    print('False')