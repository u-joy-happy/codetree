n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# Please write your code here.
A.sort()
B.sort()

same_flag = True
for i in range(n):
    if A != B :
        same_flag = False
    
print('Yes' if same_flag else 'No')
    