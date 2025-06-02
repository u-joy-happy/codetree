N = int(input())

# Please write your code here.

def print_fluct(n) :
    if n == 0 :
        return
    print(n, end=' ')
    print_fluct(n-1)
    print(n, end=' ')

print_fluct(N)