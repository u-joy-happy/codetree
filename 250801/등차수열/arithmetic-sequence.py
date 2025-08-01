n = int(input())
a = list(map(int, input().split()))

# Please write your code here.

a.sort()

max_val = 0
for x in range(1, 101):
    cnt = 0
    for i in range(n):
        for j in range(i+1, n):
            if (a[i] + a[j]) / 2 == x:
                cnt += 1
    max_val = max(max_val, cnt)

print(max_val)