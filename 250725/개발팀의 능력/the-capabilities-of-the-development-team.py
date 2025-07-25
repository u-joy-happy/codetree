arr = list(map(int, input().split()))

# Please write your code here.

res = 2 * 1000
flag = False
sum_val = sum(arr)

for i in range(5):
    for j in range(5):
        for k in range(5):
            if i == j or k == i or k == j :
                continue
            sum1 = arr[i] + arr[j]
            sum2 = sum_val - sum1 - arr[k]
            max_val = max(sum1, sum2, arr[k])
            min_val = min(sum1, sum2, arr[k])
            if sum1 == sum2 or sum2 == arr[k] or sum1 == arr[k]:
                continue
            diff = max_val - min_val
            if res > diff :
                res = diff
                flag = True

print(res if flag else -1)
