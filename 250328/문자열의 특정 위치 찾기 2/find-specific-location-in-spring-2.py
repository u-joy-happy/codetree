a = input()
arr = ['apple', 'banana', 'grape', 'blueberry', 'orange']
cnt = 0

for item in arr :
    if item[2] == a or item[3] == a :
        cnt += 1
        print(item)

print(cnt)