n1, n2 = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

if b[0] in a :
    first_idx = a.index(b[0])
    if a[first_idx : first_idx + n2] == b :
        print('Yes')
    else :
        print('No')
else :
    print('No')