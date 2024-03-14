"""
#By listing the first six prime numbers: 2,3,5,7,11, and 13.
#we can see that the 6th prime is 13.
#What is the 10001st prime number?
"""
def sieve_of_eratosthenes(n):
  """
  Finds all prime numbers up to a given limit 'n' using the Sieve of Eratosthenes.
  """
  # Create a list of booleans, initially all True (assuming all numbers are prime)
  is_prime = [True] * (n + 1)
  is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime

  # Iterate through potential prime factors (up to the square root of n)
  for i in range(2, int(n**0.5) + 1):
    if is_prime[i]:
      # Mark all multiples of the current prime factor as non-prime
      for j in range(i * i, n + 1, i):
        is_prime[j] = False

  # Count prime numbers
  prime_count = 0
  for i in range(2, n + 1):
    if is_prime[i]:
      prime_count += 1
      # Check if the count reaches the 10001st prime
      if prime_count == 10001:
        return i

# Find the 10001st prime number (increase limit to ensure finding it)
prime_number = sieve_of_eratosthenes(1000000)  # Increase limit as needed

# Print the result
print(prime_number)
 