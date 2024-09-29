a = 13195
b = 2
lst = []
while a != 1:
    if a % b == 0:
        a = a/b
        lst.append(b)
    else:
        b += 1
print(lst)