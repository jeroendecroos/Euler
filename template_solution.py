"""A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""
import sys
import unittest
import math



def find_special_pythagorean_triplet_brute(length_sequence):
    pass

def find_special_pythagorean_triplet_site(length_sequence):
    raise Exception('No site solution provided')


def find_special_pythagorean_triplet(length_sequence, algorithm='brute'):
    if algorithm=='brute':
        answer = find_special_pythagorean_triplet_brute(length_sequence)
    elif algorithm=='site':
        answer = find_special_pythagorean_triplet_site(length_sequence)
    else:
        raise Exception("Unknown algorithm %s" % algorithm)
    return answer

class TestSpecialPythagoreanTriplet(unittest.TestCase):
    def test_brute_force(self):
        self.assertEqual(find_special_pythagorean_triplet(12,'brute'), 60)


if __name__ == '__main__':
    number = int(sys.argv[1])
    if len(sys.argv) < 3:
        answer = find_special_pythagorean_triplet(number)
    else:
        answer = find_special_pythagorean_triplet(number, sys.argv[2])
    print 'answer=%r' % answer



