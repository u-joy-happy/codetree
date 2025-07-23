n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
res = 0
for i in range(n):
    for j in range(i, n):
        avg_val = sum(arr[i:j+1]) / (j - i + 1)
        for k in range(i, j+1):
            if avg_val == arr[k]:
                res += 1
                break
print(res)        
        
        