a = input()

cod = ord(a) + 1

if cod > ord('z') :
    cod = ord('a')

print(chr(cod))