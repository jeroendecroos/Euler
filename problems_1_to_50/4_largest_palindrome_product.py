"""A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.
Find the largest palindorme made from the product of two 3-digit numbers.
"""
import sys
import unittest


def find_largest_palindrome_product_brute(minumum_multiplier, maximum_multiplier):
    return 0

def find_largest_palindrome_product(number_of_digits, algorithm='brute'):
    maximum_multiplier = (10**number_of_digits)-1
    minimum_multiplier = 10**(number_of_digits-1)
    if algorithm=='brute':
        answer = find_largest_palindrome_product_brute(minimum_multiplier, maximum_multiplier)
    else:
        raise Exception("Unknown algorithm %s" % algorithm)
    return answer


class TestLargestPalindromeProduct(unittest.TestCase):
    def test_brute_force(self):
        self.assertEqual(find_largest_palindrome_product(2,'brute'), (91,99,9009))

if __name__ == '__main__':
    number = int(sys.argv[1])
    print 'answer=%d' % find_largest_palindrome_product(number)



