a = input()

cnt1, cnt2 = 0, 0

for i in range(len(a)-1) :
    if a[i] + a[i + 1] == 'ee':
        cnt1 += 1
    if a[i] + a[i + 1] == 'eb':
        cnt2 += 1

print(cnt1, cnt2)