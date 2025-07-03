N = input()

# Please write your code here.

def to_decimal(n):
    num = 0
    for item in n:
        num = num * 2 + int(item)
    return num

def to_binary(n):
    num = ''
    while True:
        if n < 2 :
            num += str(n)
            break
        num += str(n % 2)
        n //= 2
    return num[::-1]

print(to_binary(to_decimal(N)*17))