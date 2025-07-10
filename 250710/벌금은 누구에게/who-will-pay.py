N, M, K = map(int, input().split())
student = [int(input()) for _ in range(M)]

# Please write your code here.

arr = [K] * N

for i in range(M) :
    arr[student[i]-1] -= 1
    if arr[student[i]-1] == 0 :
        print(arr[student[i]])
        break

