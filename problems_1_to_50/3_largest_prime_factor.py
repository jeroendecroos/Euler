"""The prime factors of 13195 are 5,7,13,29
What is the largest prime factor of the number 6008551475143
"""
import sys
import unittest

def sief_prime_generator(max_prime, known_primes=()):
    sief = [0]*max_prime
    for prime in sorted(known_primes):
       for disable_count in xrange(prime, max_prime+1,prime):
            sief[disable_count-1] = 1
    count = 2
    while count <= max_prime:
        index = count -1
        if not sief[index]:
            yield count
            for disable_count in xrange(count, max_prime+1,count):
                sief[disable_count-1] = 1
        count += 1

KNOWN_PRIMES = set()
def number_is_prime(number):
    global KNOWN_PRIMES
    prime_generator = sief_prime_generator( number, KNOWN_PRIMES)
    primes = [x for x in prime_generator] 
    KNOWN_PRIMES = KNOWN_PRIMES.union(set(primes))
    if number == primes[-1]:
        return True
    else:
        return False

def get_lowest_undividable(number, divisor):
    """ Divide number with divisor until result is not integer
    """
    while not number % divisor:
        number /= divisor
    return number

def prime_factor_generator(number):
    maximum_factor = number
    divisor = 2
    while divisor <= number:
        if not number % divisor:
            if number_is_prime(divisor):
                yield divisor
                number = get_lowest_undividable(number, divisor)
        divisor += 1 

def find_largest_prime_factor_brute(number):
    prime_factors = [x for x in prime_factor_generator(number)]
    if prime_factors:
        return prime_factors[-1]
    else: 
        return []

def find_largest_prime_factor_site(number):
    """ Every found factor will be by default prime if number is unlimited (!) divided by found factors:
        20 -> prime: 2  
            -> 20 /2 /2 = 5
               prime 5
    """
    if not number%2:
        last_factor = 2
        number = get_lowest_undividable(number, 2)
    else:
        last_factor = 1
    factor = 3
    maximum_factor = number**(1.0/2)
    while number > 1 and factor <= maximum_factor:
        if not number%factor:
            last_factor = factor
            number = get_lowest_undividable(number, factor)
            maximum_factor = number**(1.0/2)
        factor += 2
    if number ==1:
        return last_factor
    else:
        return number    


def find_largest_prime_factor(number, algorithm='site_solution'):
    if algorithm == 'brute':
        answer = find_largest_prime_factor_brute(number)
    elif algorithm == 'site_solution':
        answer = find_largest_prime_factor_site(number) 
    else:
        raise Exception('unknown algorithm {}'.format(algorithm))
    return answer

class TestSiefPrimeGenerator(unittest.TestCase):
    def test_sief_generator(self):
        sief_generator_list = (lambda maximum: [x for x in sief_prime_generator(maximum)])
        self.assertEqual(sief_generator_list(0), [])
        self.assertEqual(sief_generator_list(1), [])
        self.assertEqual(sief_generator_list(2), [2])
        self.assertEqual(sief_generator_list(3), [2,3])
        self.assertEqual(sief_generator_list(10), [2,3,5,7])

class TestLargestPrimeFactor(unittest.TestCase):
    def test_brute_force(self):
        self.assertEqual(find_largest_prime_factor(13195,'brute'), 29)
        self.assertEqual(find_largest_prime_factor(600851475143,'brute'), 6857)
    def test_site_solution(self):
        self.assertEqual(find_largest_prime_factor(13195,'site_solution'), 29)
        self.assertEqual(find_largest_prime_factor(600851475143,'site_solution'), 6857)


if __name__ == '__main__':
    number = int(sys.argv[1])
    print 'answer=%d' % find_largest_prime_factor(number)



