a = input()

# Please write your code here.

def to_decimal(num):
    res = 0
    for n in num:
        res = (res * 2) + int(n)
    return res

flag = True
bi = ''
for i in a:
    if i == '0' and flag :
        bi += '1'
        flag = False
    else :
        bi += i

print(to_decimal(bi))