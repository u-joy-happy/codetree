arr = [list(map(int, input().split())) for _ in range(2)]

# tot_sum_val = [0]*3

# for i in range(2):
#     tot_sum_val[0][i] = sum(arr[i])
#     tot_sum_val[2] += sum(arr[i])

# for j in range(4):
#     tot_sum_val[1][i] = sum([arr[i][j] for i in range(2)])

avg_horz = [0] *2
avg_vert = [0] *4
avg_tot = 0

for i in range(2):
    avg_horz[i] = sum(arr[i])/4
    avg_tot += sum(arr[i])/4
avg_tot /= 2

for i in range(4):
    avg_vert[i] = (arr[0][i] + arr[1][i])/2


for avg in avg_horz :
    print(f'{avg:.1f}', end=' ')
print()

for avg in avg_vert :
    print(f'{avg:.1f}', end=' ')
print()

print(f'{avg_tot:.1f}')