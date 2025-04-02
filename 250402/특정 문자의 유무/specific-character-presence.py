a = input()
flag1 = False 
flag2 = False 

for i in range(len(a)-1) :
    if a[i:i+2] == 'ee' :
        flag1 = True
    if a[i:i+2] == 'ab' :
        flag2 = True

if flag1 : print('Yes', end=' ')
else: print('No', end=' ')

if flag2 : print('Yes')
else: print('No')