n = int(input())
name = []
street_address = []
region = []

for _ in range(n):
    n_i, s_i, r_i = input().split()
    name.append(n_i)
    street_address.append(s_i)
    region.append(r_i)

# Please write your code here.
class Person :
    def __init__(self, name, street_address, region):
        self.name = name
        self.street_address = street_address
        self.region = region

max_idx = 0
pp = []
for i in range(n) :
    pp.append(Person(name[i], street_address[i], region[i]))
    if name[i] > name[max_idx] :
        max_idx = i

print(f'name {pp[max_idx].name}')
print(f'addr {pp[max_idx].street_address}')
print(f'city {pp[max_idx].region}')