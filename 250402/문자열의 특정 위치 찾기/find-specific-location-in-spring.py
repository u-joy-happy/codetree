a, b = input().split()
flag = False 

for i in range(len(a)) :
    if a[i] == b :
        print(i)
        flag = True
        break 

if not flag :
    print('No')