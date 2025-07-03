n = int(input())

# Please write your code here.

digit = []

while True :
    if n == 1 :
        digit.append(1)
        break
    
    digit.append(n % 2)
    n //= 2


for item in digit[::-1]:
    print(item, end='')