n1, n2 = map(int, input().split())

arr = list(map(int, input().split()))
brr = list(map(int, input().split()))

# if b[0] in a :
#     first_idx = a.index(b[0])
#     if a[first_idx : first_idx + n2] == b :
#         print('Yes')
#     else :
#         print('No')
# else :
#     print('No')

idx = 0
flag = False

for a in arr :
    if a != brr[idx] :
        idx = 0
        flag = False
        continue

    idx += 1

    if n2 == idx :
        flag = True
        break

if flag :
    print('Yes')
else :
    print('No')