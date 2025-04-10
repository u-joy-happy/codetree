s = input()

first = s[0]
second = s[1]
new_str = ''

for item in s :
    if item == second :
        new_str += first
    else :
        new_str += item

print(new_str)