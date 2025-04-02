string = input()
new_string = ''

for a in string[1::2] :
    new_string = a + new_string

print(new_string)