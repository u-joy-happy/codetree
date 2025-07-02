a, b, c, d = map(int, input().split())

# Please write your code here.

st_time = a * 60 + b
ed_time = c * 60 + d

diff = ed_time - st_time

print(diff)