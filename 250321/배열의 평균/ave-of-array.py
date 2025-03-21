arr = [list(map(int, input().split())) for _ in range(2)]
avg_tot = 0

for i in range(2):
    avg_horz = sum(arr[i])/4
    print(f'{avg_horz:.1f}', end=' ')
    avg_tot += sum(arr[i])/4
print()

for i in range(4):
    avg_vert = (arr[0][i] + arr[1][i])/2
    print(f'{avg_vert:.1f}', end=' ')
print()

avg_tot /= 2
print(f'{avg_tot:.1f}')