lst = []
prod = []

for i in range(100, 1000):
    for j in range(100, 1000):
        lst.append(i*j)

for stuff in lst:
    if str(stuff) == str(stuff)[::-1]:
        prod.append(stuff)

print(max(prod))