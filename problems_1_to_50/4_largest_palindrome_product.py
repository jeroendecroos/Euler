"""A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.
Find the largest palindorme made from the product of two 3-digit numbers.
"""
import sys
import unittest

def is_palindrome(number):
    number_str = str(number)
    if number_str == number_str[::-1]:
        return True
    return False    

def find_largest_palindrome_product_brute(minimum_multiplier, maximum_multiplier):
    multiples = set()
    for x in xrange(maximum_multiplier, minimum_multiplier-1, -1):
        for y in xrange(x, minimum_multiplier-1, -1):
            z = x*y
            multiples.add(z)
    for multiple in sorted(multiples, reverse=True):
        if is_palindrome(multiple):
            return multiple
    return 0

def find_largest_palindrome_product_site(minimum_multiplier, maximum_multiplier):
    if maximum_multiplier < 11:
        raise Exception('algorithm doesnt work for small numbers')
    largest_palindrome = 0
    a = maximum_multiplier
    while a >= minimum_multiplier:
        if not a%11:   ### At least one of the factors must have factor 11
            b = maximum_multiplier
            delta_b = 1
        else:
            b = maximum_multiplier/11*11   # largest number divisible by 11
            delta_b = 11
        while b >= a:
            multiple = a*b
            if multiple <= largest_palindrome:
                break
            elif is_palindrome(multiple):
                largest_palindrome = multiple
            b -= delta_b
        a -= 1
    return largest_palindrome

def find_largest_palindrome_product(number_of_digits, algorithm='site_solution'):
    maximum_multiplier = (10**number_of_digits)-1
    minimum_multiplier = 10**(number_of_digits-1)
    if algorithm=='brute':
        answer = find_largest_palindrome_product_brute(minimum_multiplier, maximum_multiplier)
    elif algorithm=='site_solution':
        answer = find_largest_palindrome_product_site(minimum_multiplier, maximum_multiplier)
    else:
        raise Exception("Unknown algorithm %s" % algorithm)
    return answer


class TestLargestPalindromeProduct(unittest.TestCase):
    def test_brute_force(self):
        self.assertEqual(find_largest_palindrome_product(2,'brute'), 9009)
        self.assertEqual(find_largest_palindrome_product(3,'brute'), 906609)
    def test_site_solution(self):
        self.assertEqual(find_largest_palindrome_product(2,'site_solution'), 9009)
        self.assertEqual(find_largest_palindrome_product(3,'site_solution'), 906609)


if __name__ == '__main__':
    number = int(sys.argv[1])
    print 'answer=%d' % find_largest_palindrome_product(number)



