for _ in range(5):
    t = ord('a') - ord('A')
    arr = [chr(ord(a) - t) for a in input().split()]

    for a in arr :
        print(a, end=' ')
    
    print()
    