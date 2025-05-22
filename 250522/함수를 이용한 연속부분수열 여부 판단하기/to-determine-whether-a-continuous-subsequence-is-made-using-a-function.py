n1, n2 = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# Please write your code here.

def is_subsequence(a, b, n1, n2) :
    for i in range(n1) :
        if a[i] != b[0] :
            continue
        if a[i:i+n2] == b :
            return True
    return False

if is_subsequence(a, b, n1, n2) :
    print('Yes')
else :
    print('No')