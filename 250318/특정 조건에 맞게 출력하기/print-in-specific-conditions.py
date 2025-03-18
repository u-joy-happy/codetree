arr = map(int, input().split())

for a in arr :
    if a == 0 :
        break
    elif a % 2 == 0 :
        print(a//2, end=' ')
    else :
        print(a+3, end=' ')
    