flag = int(input('Enter'))
a = 1
b = 0
c = 0
d = 0
while flag != 0:
    c = a + b
    a = a + b
    b = c - b
    d += c
    print(c)
    flag -= 1 
print(d)
    