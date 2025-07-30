n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.

res_arr = [[0] for _ in range(10)]
for i in range(6) :
    for j in range(n):
        digit = arr[j] // (1 * (10 ** i)) % 10
        res_arr[digit].append(arr[j])
    
    new_arr = []
    for k in range(10):
        for item in res_arr[k]:
            if item == 0 :
                continue
            new_arr.append(item)
    arr = new_arr

for item in arr :
    print(item, end=' ')