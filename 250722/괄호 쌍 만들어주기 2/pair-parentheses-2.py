A = input()

# Please write your code here.

cnt = 0
for i in range(len(A)-1):
    for j in range(i, len(A)-1):
        if A[i]+A[i+1] == '((' and A[j]+A[j+1] =='))':
            cnt += 1

print(cnt)