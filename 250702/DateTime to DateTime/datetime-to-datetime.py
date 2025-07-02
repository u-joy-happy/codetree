a, b, c = map(int, input().split())

# Please write your code here.

st_time = 11 + 11 * 60 + 11 * 60 * 24
ed_time = c + b * 60 + a * 60 * 24

print(ed_time - st_time if ed_time - st_time > 0 else -1 )