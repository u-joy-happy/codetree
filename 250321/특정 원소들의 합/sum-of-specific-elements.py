arr = [list(map(int, input().split())) for _ in range(4)]

tot_sum = 0

for i in range(4):
    for j in range(i+1):
        tot_sum += arr[i][j]

print(tot_sum)