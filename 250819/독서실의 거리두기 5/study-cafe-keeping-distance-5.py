N = int(input())
seat = input()

# Please write your code here.

max_val = 0
prev = -1

for i in range(N):
    next = -1
    if seat[i] == '1':
        prev = i
        continue
    for j in range(i, N) :
        if seat[j] == '1' :
            next = j
            break

    if prev < 0 :
        diff = next
    elif next < 0 :
        diff = (N-1) - prev
    else:
        diff = min(i - prev, next - i)
    max_val = max(max_val, diff)

print(max_val)