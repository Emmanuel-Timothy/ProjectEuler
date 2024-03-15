"""
The sum of the primes below 10 is 2+3+5+7 = 17.
Find the sum of all the primes below two million.
"""

def sieve_of_eratosthenes_sum(n):
    """
    Finds the sum of all prime numbers up to a given limit 'n' using the Sieve of Eratosthenes.
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

    # Sum prime numbers
    prime_sum = 0
    for i in range(2, n + 1):
        if is_prime[i]:
            prime_sum += i

    return prime_sum

# Find the sum of all prime numbers below two million
n = 2000000
sum_of_primes = sieve_of_eratosthenes_sum(n)

# Print the result
print("The sum of all prime numbers below", n, "is:", sum_of_primes)
