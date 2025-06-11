N = int(input())

# Please write your code here.

def get_n_arr(n) :
    if n == 1 or n == 2 :
        return n
    return get_n_arr(n//3) + get_n_arr(n-1)

print(get_n_arr(N))