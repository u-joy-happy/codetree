s, q = input().split()
q = int(q)

for _ in range(q):
    query, a, b = input().split()
    query = int(query)
    new_str = ''

    if query == 1:
        a, b = int(a)-1, int(b)-1
        if a > b :
            a, b = b, a
        new_str = s[:a] + s[b] + s[a+1:b] + s[a] + s[b+1:]
    else :
        for item in s :
            if item == a :
                new_str += b
            else :
                new_str += item
    s = new_str
    print(s)