flag = False

arr = [input() for _ in range(10)]
a = input()

for item in arr :
    if item[-1] == a:
        print(item)
        flag = True
    
if not flag :
    print('None')