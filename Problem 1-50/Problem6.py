"""
#The sum of the squares of the first ten natural numbers is, 1^2+2^2+...+10^2=385.
#The square of the sum of the first ten natural numbers is, (1+2+...+10)^2=55^2=3025.
#Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025−385=2640.
#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""
def sum_of_squares(n):
  """
  Calculates the sum of squares of natural numbers up to 'n'.
  """
  return n * (n + 1) * (2 * n + 1) // 6

def square_of_sum(n):
  """
  Calculates the square of the sum of natural numbers up to 'n'.
  """
  return (n * (n + 1) // 2) ** 2

# Limit (first 100 natural numbers)
limit = 100

# Calculate sum of squares and square of sum
sum_squares_val = sum_of_squares(limit)
square_sum_val = square_of_sum(limit)

# Find the difference
difference = square_sum_val - sum_squares_val

# Print the result
print(difference)
 