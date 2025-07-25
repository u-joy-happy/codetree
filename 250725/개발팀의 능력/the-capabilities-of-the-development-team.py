arr = list(map(int, input().split()))

# Please write your code here.

flag = False
res = 2 * 1000

for i in range(5):
    for j in range(5):
        for k in range(5):
            for l in range(5):
                for m in range(5):
                    if i == j or k == i or k == j or l == i or l == j or l == k or m == i or m == j or m == k or m == l: 
                        continue
                    sum1 = arr[i] + arr[j]
                    sum2 = arr[k] + arr[l]
                    if sum1 == sum2 or sum1 == arr[m] or sum2 == arr[m]:
                        continue
                    max_val = max(sum1, sum2, arr[m])
                    min_val = min(sum1, sum2, arr[m])
                    diff = max_val - min_val
                    if res > diff:
                        res = diff
                        flag = True

print(res if flag else -1)
