"""
The prime factors of 13195 are 5,7,13 and 29 .
What is the largest prime factor of the number 600851475143?
"""
def is_prime(num):
  """
  Checks if a number is prime.
  """
  if num <= 1:
    return False
  for i in range(2, int(num**0.5) + 1):
    if num % i == 0:
      return False
  return True

def largest_prime_factor(num):
  """
  Finds the largest prime factor of a number.
  """
  if num <= 1:
    return None
  i = 2
  while i * i <= num:
    while num % i == 0:
      num //= i
    i += 1
  return num

# Target number
number = 600851475143

# Find the largest prime factor
largest_factor = largest_prime_factor(number)

# Print the result
print(largest_factor)
