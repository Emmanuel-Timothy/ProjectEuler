# Define the upper limit
limit = 1000

# Find the sum of multiples of 3 and 5 below the limit
sum_of_multiples = 0
for num in range(1, limit):
  if num % 3 == 0 or num % 5 == 0:
    sum_of_multiples += num

# Print the final sum
print(sum_of_multiples)
