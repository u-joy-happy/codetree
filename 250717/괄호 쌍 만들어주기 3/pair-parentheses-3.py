A = input()

# Please write your code here.
cnt = 0
for a in range(len(A)):
    if A[a] == '(':
        for b in range(a+1, len(A)):
            if A[b] == ')':
                cnt += 1

print(cnt)