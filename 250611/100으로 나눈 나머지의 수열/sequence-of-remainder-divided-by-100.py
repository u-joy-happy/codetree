N = int(input())

# Please write your code here.

def get_div_arr(n):
    if n == 1 or n == 2:
        return n * 2 
    return get_div_arr(n-1) * get_div_arr(n-2) % 100

print(get_div_arr(N))
        