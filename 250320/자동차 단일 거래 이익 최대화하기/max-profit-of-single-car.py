n = int(input())
price = list(map(int, input().split()))

# Please write your code here.

max_rev = 0

for i in range(n-1):
    for j in range(i+1, n) :
        if price[j] - price[i] > max_rev :
            max_rev = price[j] - price[i]

print(max_rev)