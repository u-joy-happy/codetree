n = int(input())
cnt = 0
length = 0

for _ in range(n):
    a = input()
    length += len(a)
    if a[0] == 'a' :
        cnt += 1
    
print(length, cnt)