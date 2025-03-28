a = input()
b = input()
new_str =''

for i in a+b :
    if i == ' ' :
        continue
    new_str += i

print(new_str)