N = int(input())

# Please write your code here.

def power_sum(n):
    if n < 10 :
        return n * n
    return power_sum(n // 10) + ((n % 10) * (n % 10))

print(power_sum(N))