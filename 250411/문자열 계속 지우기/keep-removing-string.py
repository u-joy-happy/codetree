A = input()
B = input()

# Please write your code here.

flag = True

while flag :
    for i in range(len(A) - len(B) + 1):
        tar = A[i:i+len(B)]
        org = A
        if B == tar :
            A = A[:i] + A[i+len(B):]
            break
    if A == org :
        flag = False

print(A)