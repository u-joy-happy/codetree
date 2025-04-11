a = input()
idx = a.find('e')

arr = list(a)
arr.pop(idx)
a = ''.join(arr)

print(a)
