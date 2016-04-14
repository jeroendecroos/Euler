"""The sum of the squares of the first ten natural numbers is,
    1**2 + 2**2 + ... + 10 ** 2 = 385
The square of the sum of the first ten natural number is,
    (1 + 2 + ... + 10)**2 = 55**2 = 3025
Hence the difference between the sum of the squares aof the first ten natural numbers and the square of the sum is 3025-385=2640
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum
"""
import sys
import unittest
import math

from ..lib import prime_numbers


def find_10001st_prime_brute(number):
    count = 0
    i = 3
    primes = [2]
    while len(primes) != number:
        prime = True
        for p in primes:
            if not i%p:
                prime = False
                break
        if prime:
            primes.append(i)
        i+=1
    return primes[-1]

def find_10001st_prime_site(number):
    count = 1
    candidate = 1
    while count!=number:
        candidate +=2
        if is_prime_site(candidate):
            count+=1
    return candidate

def is_prime_site(n):
    if n==1: 
        return False
    elif n<4:
        return True
    elif not n%2:
        return False
    elif n<9:
        return True
    elif not n%3:
        return False
    else:
        r = math.floor(n**(1./2))
        f = 5
        while f <=r:   
            if not n%f:
                return False
            elif not n%(f+2):
                return False
            f+=6
        return True
    

def find_10001st_prime(max_value, algorithm='brute'):
    if algorithm=='brute':
        answer = find_10001st_prime_brute(max_value)
    elif algorithm=='site':
        answer = find_10001st_prime_site(max_value)
    else:
        raise Exception("Unknown algorithm %s" % algorithm)
    return answer


class TestFind10001stPrime(unittest.TestCase):
    def test_brute_force(self):
        self.assertEqual(find_10001st_prime(6,'brute'), 13)
        self.assertEqual(find_10001st_prime(10001,'brute'), 104743)


if __name__ == '__main__':
    number = int(sys.argv[1])
    if len(sys.argv) < 3:
        answer = find_10001st_prime(number)
    else:
        answer = find_10001st_prime(number, sys.argv[2])
    print 'answer=%r' % answer



