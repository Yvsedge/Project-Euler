# largest prime factors of 600851475143

a = 600851475143
b = 2

while a != 1:
    if a % b == 0:
        a = a/b
    else:
        b += 1
print(b)