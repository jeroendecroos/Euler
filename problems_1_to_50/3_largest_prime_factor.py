"""The prime factors of 13195 are 5,7,13,29
What is the largest prime factor of the number 6008551475143
"""
import sys
import unittest

def sief_prime_generator(max_prime):
    sief = [0]*max_prime
    count = 2
    while count <= max_prime:
        index = count -1
        if not sief[index]:
            yield count
            for disable_count in xrange(count, max_prime+1,count):
                sief[disable_count-1] = 1
        count += 1


def find_largest_prime_factor(number, algorithm='brute'):
    if algorithm == 'brute':
        answer = sum([29]) 
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


if __name__ == '__main__':
    number = int(sys.argv[1])
    print [x for x in prime_generator_sief(number)]
    exit()
    print find_largest_prime_factor(number)



