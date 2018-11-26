from math import sqrt
from pprint import pprint as pp

from itertools import islice, count

def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

#prime_square_divisior = {x*x: (1, x, x*x)  for x in range(201) if is_prime(x)}
#pp(prime_square_divisior)

thousand_primes = islice((x for x in count() if is_prime(x)), 1000)

print (thousand_primes)

# print(list(thousand_primes))

# some of first 1000 prime numbers
print(sum(islice((x for x in count() if is_prime(x)), 1000)))

# is there any prime number between 1328 and 1360 inclusive?

print (any(is_prime(x) for x in range(1328, 1360)))

# Check that all of these city names are proper nouns with initial upper-case letter
result = all(name == name.title() for name in ['London', 'Paris', 'Tokyo', 'New York', 'Sydney', 'Kuala Lumpur'])
print(result)
