a = input()
first = a[0]
second = a[1]
new_str = ''

for item in a :
    if item == first :
        new_str += second
    elif item == second :
        new_str += first
    else :
        new_str += item

print(new_str)

