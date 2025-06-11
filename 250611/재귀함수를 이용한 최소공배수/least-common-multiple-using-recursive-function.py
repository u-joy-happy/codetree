n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.

def GCD(a, b):
    if b == 0 :
        return a
    return GCD(b, a % b)

def LCM(i) :
    if i == 0 :
        return arr[i]
    return LCM(i-1) * arr[i-1] // GCD(LCM(i-1), arr[i-1])


print(LCM(n))