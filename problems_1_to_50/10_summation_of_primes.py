"""The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""
import sys
import unittest

from ..lib import prime_numbers


def find_summation_of_primes_brute(max_prime):
    primes = [x for x in prime_numbers.sief_prime_generator(max_prime) ] 
    return sum(primes)

def find_summation_of_primes_site(max_prime):
    primes = [x for x in prime_numbers.sief_prime_generator_site(max_prime)]
    return sum(primes)

def find_summation_of_primes(max_prime, algorithm='brute'):
    if algorithm=='brute':
        answer = find_summation_of_primes_brute(max_prime)
    elif algorithm=='site':
        answer = find_summation_of_primes_site(max_prime)
    else:
        raise Exception("Unknown algorithm %s" % algorithm)
    return answer

class TestSummationOfPrimes(unittest.TestCase):
    def _test_template_example(self, algorithm):
        self.assertEqual(find_summation_of_primes(10, algorithm), 17)

    def _test_template_solution(self, algorithm):
        pass
        self.assertEqual(find_summation_of_primes(2000000, algorithm), 142913828922)

    @unittest.expectedFailure
    def test_site_example(self):
        self._test_template_example('site')
    def test_site_solution(self):
        self._test_template_solution('site')
    def test_brute_example(self):
        self._test_template_example('brute')
    def test_brute_solution(self):
        self._test_template_solution('brute')


if __name__ == '__main__':
    number = int(sys.argv[1])
    if len(sys.argv) < 3:
        answer = find_summation_of_primes(number)
    else:
        answer = find_summation_of_primes(number, sys.argv[2])
    print 'answer=%r' % answer



