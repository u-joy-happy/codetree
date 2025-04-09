a = input()

new_str = a[:1] + 'a' + a[2:]
new_str = new_str[:-2] + 'a' + new_str[-1:]

print(new_str)