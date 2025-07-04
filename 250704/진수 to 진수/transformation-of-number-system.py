a, b = map(int, input().split())
n = input()

# Please write your code here.

num = 0
for i in n :
    num = num * a + int(i)

res = []
while True :
    if num < b :
        res.append(num)
        break
    res.append(num%b)
    num //= b

for item in res[::-1] :
    print(item, end='')