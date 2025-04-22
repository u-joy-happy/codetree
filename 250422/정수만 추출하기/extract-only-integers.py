a, b = input().split()
num1, num2 = '', ''

for i in a :
    if not (i >= '0' and i <= '9') :
        break
    num1 += i

for i in b :
    if not (i >= '0' and i <= '9') :
        break
    num2 += i

print(int(num1) + int(num2))

