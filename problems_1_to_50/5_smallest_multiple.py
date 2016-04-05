"""2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder. 

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""
import sys
import unittest


def find_smallest_multiple_brute(max_divisor):
    """Idea : 12 is divisable by 2,3,4   == 3 * 2**2 -> expresion of primes because 4 ==2**2
        find if number is prime, if not -> find amount of primes needed
    """
    prime_map = {}
    for divisor in xrange(2,max_divisor):
#        primes = find_prime_factors(max_divisor)
#        if primes[0] == divisor:
#            prime_map[divisor] == 2


def find_smallest_multiple(max_divisor, algorithm='brute'):
    if algorithm=='brute':
        answer = find_smallest_multiple_brute(max_divisor)
    else:
        raise Exception("Unknown algorithm %s" % algorithm)
    return answer


class TestLargestPalindromeProduct(unittest.TestCase):
    def test_brute_force(self):
        self.assertEqual(find_smallest_multiple(10,'brute'), 2520)

if __name__ == '__main__':
    number = int(sys.argv[1])
    print 'answer=%d' % find_smallest_multiple(number)



