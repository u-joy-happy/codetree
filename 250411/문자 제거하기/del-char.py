a = input()

while len(a) > 1 :
    n = int(input())
    if n >= len(a):
        n = len(a) - 1
    
    arr = list(a)
    arr.pop(n)
    a = ''.join(arr)
    
    print(a)
    
