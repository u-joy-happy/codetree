s = input()
arr = list(s)

arr.pop(1)
arr.pop(len(arr)-2)

print(''.join(arr))