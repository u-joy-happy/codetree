X, Y = map(int, input().split())

# Please write your code here.

def palindrome(n):
    o, r = str(n), str(n)[::-1]
    return o == r

cnt = 0
for i in range(X, Y+1):
    if palindrome(i) :
        cnt +=1
print(cnt)