n = int(input())
cnt_val = 0
sum_val = 0

arr = [input() for _ in range(n)]
start = input()

for item in arr :
    if item[0] == start :
        cnt_val += 1
        sum_val += len(item)

print(f'{cnt_val} {sum_val/cnt_val:.2f}')