""" For testing certain syntax """
import math



def prime_factors(n):
    factors = []
    # Handle the case of 2 as a factor
    while n % 2 == 0:
        factors.append(2)
        n //= 2

    # Iterate through odd numbers starting from 3 up to the square root of n
    # We only need to check up to the square root because if a number has
    # a prime factor greater than its square root, it must also have a
    # prime factor smaller than its square root.
    i = 3
    while i * i <= n:
        while n % i == 0:
            factors.append(i)
            n //= i
        i += 2  # Increment by 2 to check only odd numbers

    # If n is still greater than 2 after the loop, it means n itself is a prime factor
    if n > 2:
        factors.append(n)

    return factors


def get_primes(n):
    factors = []
    
    while n%2==0:
        factors.append(2)
        n//=2
    
    i=3
    while i*i<=n:
        while n%i==0:
            factors.append(i)
            n//=i
        
        i += 2
        
    if n > 2:
        factors.append(n)
        
    return factors
        

# Example usage:
#print(prime_factors(12))  # Output: [2, 2, 3]
#print(prime_factors(100)) # Output: [2, 2, 5, 5]
#print(prime_factors(315)) # Output: [3, 3, 5, 7]
#print(prime_factors(17))  # Output: [17]
print(get_primes(905391974))
#print(prime_factors(3))
#print(prime_factors(10002189639126351283721))
#print(get_primes(12))
#print(get_primes(905391974))