N, M, K = map(int, input().split())
student = [int(input()) for _ in range(M)]

# Please write your code here.

arr = [K] * N

res = -1
for i in student :
    arr[i-1] -= 1
    if arr[i-1] == 0 :
        res = i
        break

print(res)