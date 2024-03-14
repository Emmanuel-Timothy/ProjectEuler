"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009=91×99.
Find the largest palindrome made from the product of two 3-digit numbers.
"""
def is_palindrome(num):
  """
  Checks if a number is a palindrome.
  """
  num_str = str(num)
  return num_str == num_str[::-1]

# Define the range of 3-digit numbers
lower_limit = 100
upper_limit = 1000

# Initialize largest palindrome and product
largest_palindrome = 0
largest_product = 0

# Iterate through all combinations of 3-digit numbers
for i in range(lower_limit, upper_limit):
  for j in range(lower_limit, upper_limit):
    product = i * j
    if is_palindrome(product) and product > largest_palindrome:
      largest_palindrome = product
      largest_product = i * j

# Print the result
print(f"Largest palindrome: {largest_palindrome} (product of {largest_product})")
