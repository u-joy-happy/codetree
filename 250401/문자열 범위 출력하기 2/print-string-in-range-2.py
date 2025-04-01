a = input()
n = int(input())

if n >= len(a) :
    print(a[::-1])
else :
    print(a[len(a):len(a)-n-1:-1]) 