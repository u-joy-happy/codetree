n, k, t = input().split()
n, k = int(n), int(k)
str = [input() for _ in range(n)]

# Please write your code here.

new_arr = sorted(str)

cnt = 0
for item in new_arr :
    if item[:len(t)] != t :
        continue
    cnt += 1
    if cnt == k :
        print(item)
        break