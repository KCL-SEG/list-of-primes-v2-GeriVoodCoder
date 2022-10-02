"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    if number_of_primes <= 0:
        raise ValueError
    list = []
    prime = 2
    while 1:
        if len(list) < number_of_primes:
            for i in range(2,prime):
                if prime % i == 0:
                    prime += 1
                    break
            else:
                list.append(prime)
                prime += 1
        else:
            break
    return list
