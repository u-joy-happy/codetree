a, b = map(int, input().split())

# Please write your code here.

def get_power(a, b):
    val = 1
    for _ in range(b):
        val *= a
    return val

print(get_power(a, b))

