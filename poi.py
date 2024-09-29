flag = int(input('enter '))

a = 1
b , c = 0

while flag != 0:
    c = a + b
    a = c
    b = a
    flag -= 1 
    
print(c)