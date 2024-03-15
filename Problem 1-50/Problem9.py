"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
There exists exactly one Pythagorean triplet for which a + b + c = 1000. Find the product abc such that a + b + c = n.
"""
def find_pythagorean_triplet(n):
    for a in range(1, n):
        for b in range(a + 1, n):
            c = n - a - b
            if a**2 + b**2 == c**2:
                return a * b * c
    return None

# Define the value of n
n = 1000

# Find the product abc for which a + b + c = n
result = find_pythagorean_triplet(n)

# Print the result
if result is not None:
    print("The product of abc such that a + b + c =", n, "is:", result)
else:
    print("There is no Pythagorean triplet for which a + b + c =", n)
