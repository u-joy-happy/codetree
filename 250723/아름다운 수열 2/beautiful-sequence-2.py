N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# Please write your code here.

res = 0

for i in range(N-M+1):
    tmp_b = B * 1
    for j in range(i, i+M):
        for k in range(len(tmp_b)):
            if tmp_b[k] == A[j] :
                tmp_b.pop(k)
                break
    if len(tmp_b) == 0 :
        res += 1

print(res)