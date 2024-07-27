"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3,5,6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
"""


# Define the upper limit
limit = 1000

# Find the sum of multiples of 3 and 5 below the limit
sum_of_multiples = 0
for num in range(limit):
  if num % 3 == 0 or num % 5 == 0:
    sum_of_multiples += num

# Print the final sum
print(sum_of_multiples)
