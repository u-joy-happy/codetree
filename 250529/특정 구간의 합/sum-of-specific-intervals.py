n, m = map(int, input().split())
arr = list(map(int, input().split()))
queries = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.

def get_sum_val(q):
    sum_val = 0
    for item in arr[q[0]-1:q[1]] :
        sum_val += item
    return sum_val

for q in queries :
    print(get_sum_val(q))
