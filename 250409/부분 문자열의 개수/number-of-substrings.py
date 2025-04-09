a = input()
b = input()
cnt = 0

for i in range(len(a)-1):
    if a[i:i+2] == b :
        cnt += 1

print(cnt)