n = int(input())

# Please write your code here.


def print_square(n):
    val = 1
    for _ in range(n):
        for _ in range(n):
            print(val, end=' ')
            
            val += 1
            if val == 10 :
                val = 1

        print()

print_square(n)