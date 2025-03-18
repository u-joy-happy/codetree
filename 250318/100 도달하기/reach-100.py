a, b = 1, int(input())

print(a, b, sep=' ', end=' ')
while True:
    a, b = b, a+b
    print(b, end=' ')
    if b > 100 :
        break


    
