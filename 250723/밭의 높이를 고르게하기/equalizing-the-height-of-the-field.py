N, H, T = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.

min_val = 100 * 100

for i in range(N-T+1):
    sum_val = 0
    arr_tmp = arr[i:i+T]
    for j in range(T):
        while H != arr_tmp[j]:
            if arr_tmp[j] > H :
                arr_tmp[j] -= 1
            else:
                arr_tmp[j] += 1
            sum_val += 1
    min_val = min(min_val, sum_val)

print(min_val)