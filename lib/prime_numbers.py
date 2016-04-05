etsetse
def sief_prime_generator(max_prime, known_primes=()):
    sief = [0]*max_prime
    for prime in sorted(known_primes):
       for disable_count in xrange(prime, max_prime+1,prime):
            sief[disable_count-1] = 1
    count = 2
    while count <= max_prime:
        index = count -1
        if not sief[index]:
            yield count
            for disable_count in xrange(count, max_prime+1,count):
                sief[disable_count-1] = 1
        count += 1
    
