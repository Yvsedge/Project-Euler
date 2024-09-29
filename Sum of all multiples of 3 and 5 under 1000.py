#Sum of all multiples of 3 and 5 under 1000.
sum_5 = 0
sum_3 = 0

for i in range(1000):
    if i % 5 == 0:
        sum_5 += i
    elif i % 3 == 0:
        sum_3 += i

total_sum = sum_5 + sum_3

print(total_sum)