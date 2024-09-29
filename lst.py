lst = [1]
n = int(input('Enter'))
fib0 = 0
for i in range(n+1):
    fib0 = lst[i] + lst[i-1]
    lst.append(fib0)

print(sum(lst))
print(lst)
