n = int(input())
sequence = list(map(int, input().split()))

# Please write your code here.

new_seq = list(sequence)
arr = [0] * n

new_seq.sort()

for i in range(n) :
    idx = new_seq.index(sequence[i])
    arr[i] = idx + 1
    new_seq[idx] = 0

for item in arr :
    print(item, end=' ')


