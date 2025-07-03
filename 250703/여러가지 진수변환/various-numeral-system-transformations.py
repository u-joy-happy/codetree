N, B = map(int, input().split())

# Please write your code here.

num = []

while True :
    if N < B :
        num.append(N)
        break
    
    num.append(N % B)
    N //= B

for i in num[::-1]:
    print(i, end='')