#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

nat = []

reach = int(input('Enter The Limit'))
n = 1
while n <= reach:
    nat.append(n)
    n += 1
sum_of_squares = 0
square_of_sum = 0

square_of_sum = sum(nat) ** 2

for i in nat:
    sum_of_squares += i**2

print('The sum of their squares is', sum_of_squares)
print('\nThe square of their sum is ', square_of_sum)

diff = 0

if square_of_sum > sum_of_squares:
    diff = square_of_sum - sum_of_squares
else:
    diff = sum_of_squares - square_of_sum
print('Their difference is :- ', diff)
