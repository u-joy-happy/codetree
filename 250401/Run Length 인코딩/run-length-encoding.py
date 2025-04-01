A = input()

# Please write your code here.

cur_item = A[0]
cnt = 1
res = ''

for i in range(1, len(A)) :
    if A[i - 1] == A[i] :
        cnt += 1
    else : 
        res += cur_item
        res += f'{cnt}'
        cnt = 1
        cur_item = A[i]
    
    if i == len(A)-1 :
        res += cur_item
        res += f'{cnt}'


print(len(res))
print(res)