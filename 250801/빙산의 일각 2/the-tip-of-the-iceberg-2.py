n = int(input())
h = [int(input()) for _ in range(n)]

# Please write your code here.

max_val = 0
for x in range(1, max(h)):
    cnt = 0
    prev = 0
    for i in range(n):
        if h[i] - x > 0 and prev <= 0 :
            cnt += 1
        prev = h[i] - x
    max_val = max(max_val, cnt)

print(max_val)
            
