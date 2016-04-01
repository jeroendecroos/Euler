"""If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3,5,6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""
import sys

def multiple_generator(maximum=1000, multiples=[3,5]):
    i = 1
    while i < maximum:
        for multiple in multiples:
            if not i%multiple:
                yield i
                break
        i+=1

def find_sum_of_multiples_brute(maximum, multiples):
    return sum(x for x in multiple_generator(maximum, multiples))

def sum_divisible_by(multiple, maximum):
    return sum(x for x in xrange(0,maximum,multiple))

def sum_divisible_by_smart(multiple, maximum):
    p = (maximum-1)/multiple
    return multiple*p*(p+1)/2

def find_sum_of_multiples_brute2(maximum, a,b):
    a_sum = sum_divisible_by(a, maximum)
    b_sum = sum_divisible_by(b, maximum)
    a_b_sum = sum_divisible_by(a*b, maximum)
    return a_sum + b_sum - a_b_sum

def find_sum_of_multiples_smart(maximum, a,b):
    a_sum = sum_divisible_by_smart(a, maximum)
    b_sum = sum_divisible_by_smart(b, maximum)
    a_b_sum = sum_divisible_by_smart(a*b, maximum)
    return a_sum + b_sum - a_b_sum

maximum = int(sys.argv[1])
#print find_sum_of_multiples_brute(maximum, [3,5])
#print find_sum_of_multiples_brute2(maximum, 3,5)
print find_sum_of_multiples_smart(maximum, 3,5)

