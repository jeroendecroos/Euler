"""2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder. 

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""
import sys
import math
import unittest
import collections

from ..lib import prime_numbers

def get_lowest_undividable(number, divisor):
    """ Divide number with divisor until result is not integer
    """
    while not number % divisor:
        number /= divisor
    return number

def find_prime_factors(number):
    factors = [1]
    factor = 2
    maximum_factor = number**(1.0/2)
    update_number =1
    while number > 1 and factor <= maximum_factor:
        if not number%factor:
            new_number = get_lowest_undividable(number, factor)
            number_of_factors = number/new_number/factor
            number = new_number
            factors += [factor]*number_of_factors
            maximum_factor = number**(1.0/2)
            if number ==2:
                update_number = 2
        factor += update_number
    if number > 1:
        factors.append(number)
    factors.pop(0)
    return factors


def get_minimal_needed_primes(max_divisor):
    prime_map = collections.defaultdict(int)
    for divisor in xrange(2,max_divisor+1):
        primes = find_prime_factors(divisor)
        prime_frequencies = collections.Counter(primes)
        for prime, frequency in prime_frequencies.iteritems():
            if prime_map[prime] < frequency:
                prime_map[prime] = frequency
    return prime_map

def find_smallest_multiple_brute(max_divisor):
    """Idea : 12 is divisable by 2,3,4   == 3 * 2**2 -> expresion of primes because 4 ==2**2
        find if number is prime, if not -> find amount of primes needed
    """
    prime_occurances = get_minimal_needed_primes(max_divisor)
    smallest_multiple = 1
    for prime, frequency in prime_occurances.iteritems():
        smallest_multiple *= prime*frequency
    return smallest_multiple

def get_primes(max_number):
    return [x for x in prime_numbers.sief_prime_generator(max_number)]

def find_smallest_multiple_site(max_divisor):
    primes = get_primes(max_divisor)
    print primes
    exponents = [0]*len(primes)
    i =1
    check = True
    limit = max_divisor**(1.0/2)
    for i, prime in enumerate(primes):
        exponents[i] = 1
        if check:
            if prime <= limit:
                exponents[i] = math.floor(math.log(max_divisor)/math.log(primes[i]))
            else:
                check == False
        i += 1
    print zip(primes, exponents)
    N = 1
    for prime, exponent in zip(primes, exponents):
      N *= prime**exponent
    return N

def find_smallest_multiple(max_divisor, algorithm='site_solution'):
    if algorithm=='brute':
        answer = find_smallest_multiple_brute(max_divisor)
    elif algorithm == 'site_solution':
        answer = find_smallest_multiple_site(max_divisor)
    else:
        raise Exception("Unknown algorithm %s" % algorithm)
    return answer


class TestLargestPalindromeProduct(unittest.TestCase):
    def test_brute_force(self):
        self.assertEqual(find_smallest_multiple(10,'brute'), 2520)

if __name__ == '__main__':
    number = int(sys.argv[1])
    print 'answer=%r' % find_smallest_multiple(number)



