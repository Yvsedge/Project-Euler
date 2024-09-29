#Fibonnaci Numbers
# 1, 1 , 2 , 3, 5 , 8 , 13 , 21 , .......

fib = [1]
fib0 = 0
for i in range(100):
    fib0 = fib[i] + fib[i-1]
    fib.append(fib0)

sum = 0
for i in fib:
    if i <= 4000000 and i % 2 == 0:    
        sum += i
print(sum)
