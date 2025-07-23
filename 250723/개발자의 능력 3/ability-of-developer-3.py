abilities = list(map(int, input().split()))

# Please write your code here.

def get_diff(a, b, c) :
    sum1 = a + b + c 
    sum2 = sum(abilities) - sum1
    return abs(sum1 - sum2)

ll = len(abilities)
min_val = 1000000

for i in range(ll):
    for j in range(i+1, ll):
        for k in range(j+1, ll):
            min_val = min(min_val, get_diff(abilities[i], abilities[j], abilities[k]))

print(min_val)