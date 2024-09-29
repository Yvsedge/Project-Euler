lower = 1
upper = 10000000000
n = 0

for num in range(lower, upper + 1):
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           n += 1
           if n == 10001:
             print(num , end = ' ')
             break