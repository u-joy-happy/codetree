n = int(input())
arr = input().split()

num_str = ''.join(arr)

for idx, i in enumerate(num_str) :
    print(i, end='')
    if (idx + 1) % 5 == 0 :
        print()

