"""The sum of the squares of the first ten natural numbers is,
    1**2 + 2**2 + ... + 10 ** 2 = 385
The square of the sum of the first ten natural number is,
    (1 + 2 + ... + 10)**2 = 55**2 = 3025
Hence the difference between the sum of the squares aof the first ten natural numbers and the square of the sum is 3025-385=2640
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum
"""
import sys
import unittest


def find_sum_square_difference_brute(max_value):
    n = max_value*1.0
    sum_numbers = n*(n+1)/2
    sum_squares = n**3/3 + n**2/2 +n/6
    diff = sum_numbers**2 - sum_squares
#    diff = n**4/4+n**3/6+n**2/12
    return diff

def find_sum_square_difference(max_value, algorithm='brute'):
    if algorithm=='brute':
        answer = find_sum_square_difference_brute(max_value)
    elif algorithm == 'site_solution':
        answer = find_sum_square_difference_site(max_value)
    else:
        raise Exception("Unknown algorithm %s" % algorithm)
    return answer


class TestLargestPalindromeProduct(unittest.TestCase):
    def test_brute_force(self):
        self.assertEqual(find_sum_square_difference(10,'brute'), 25164150)


if __name__ == '__main__':
    number = int(sys.argv[1])
    print 'answer=%r' % find_sum_square_difference(number)



