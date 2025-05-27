A = input()

# Please write your code here.

def is_palindrome(A) :
    if A == A[::-1] :
        return True
    else :
        return False

if is_palindrome(A) :
    print('Yes')
else :
    print('No')