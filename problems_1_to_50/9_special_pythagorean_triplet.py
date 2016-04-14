"""A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""
import sys
import unittest

from fractions import gcd

def find_special_pythagorean_triplet_brute(sum_value):
    for c in range(1,sum_value+1-2):
        for b in range(1,sum_value+1-1-c):
            if b > c:   ## c needs to be biggest
                continue
            for a in range(1,sum_value+1-c-b):
                if a > b:  ### a is symmetric to b, no need to recalculate, a automaticly smaller then c
                    continue
            if a*a+b*b == c*c:
                if a+b+c == sum_value:
                    print (a,b,c)
                    return a*b*c
    raise Exception('no pythagorean triplet found')
                

def find_special_pythagorean_triplet_site(sum_value):
    half_sum_value = sum_value / 2
    max_limit = int( (half_sum_value)**(1.0/2)-1 )
    for m in xrange(2,max_limit+1):
        if half_sum_value%m == 0:
            sm = half_sum_value / m
            while sm%2 == 0:
                sm /= 2
            if m%2 == 1:
                k = m+2
            else:
                k = m+1
            while k < 2*m and k < sm:
                if sm % k == 0 and gcd(k,m) == 1:
                    d = half_sum_value/(k*m)
                    n = k-m
                    a = d*(m*m-n*n)
                    b = 2*d*m*n
                    c = d*(m*m+n*n)
                    print (a,b,c)
                    return a*b*c
                k += 2
    raise Exception('no pythagorean triplet found')



def find_special_pythagorean_triplet(sum_value, algorithm='brute'):
    if algorithm=='brute':
        answer = find_special_pythagorean_triplet_brute(sum_value)
    elif algorithm=='site':
        answer = find_special_pythagorean_triplet_site(sum_value)
    else:
        raise Exception("Unknown algorithm %s" % algorithm)
    return answer

class TestSpecialPythagoreanTriplet(unittest.TestCase):
    def _test_template_example(self, algorithm):
        self.assertEqual(find_special_pythagorean_triplet(12, algorithm), 60)

    def _test_template_solution(self, algorithm):
        self.assertEqual(find_special_pythagorean_triplet(1000, algorithm), 31875000)

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
        answer = find_special_pythagorean_triplet(number)
    else:
        answer = find_special_pythagorean_triplet(number, sys.argv[2])
    print 'answer=%r' % answer



