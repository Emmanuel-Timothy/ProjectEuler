"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""
def lcm(a, b):
  """This function finds the Least Common Multiple of two numbers."""
  return (a * b) // gcd(a, b)

def gcd(a, b):
  """This function finds the Greatest Common Divisor of two numbers."""
  while b:
    a, b = b, a % b
  return a

# Find the LCM of numbers from 1 to 20
num = 1
for i in range(2, 21):
  num = lcm(num, i)

# Print the LCM
print(num)
