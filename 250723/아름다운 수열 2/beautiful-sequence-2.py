N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# Please write your code here.

res = 0

for i in range(N-M+1):
    if sorted(A[i:i+M]) == sorted(B):
        res += 1

print(res)