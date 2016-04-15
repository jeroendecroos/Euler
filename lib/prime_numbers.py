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



def sief_prime_generator_site(max_prime, known_primes=()):
    if max_prime < 2 :
        return
    max_sieve = (max_prime-1)/2
    sieve = [0]*(max_sieve+1)
    cross_limit = int(max_prime**(1.0/2)-1)/2
    def disable_sieve( prime_index):
        i = prime_index
        begin = 2*i*(i+1)
        step = 2*i+1
        for j in xrange(begin, max_sieve+1, step):
              sieve[j] = 1
    for prime in sorted(known_primes):
        disable_sieve( (prime-1)/2 )
    if 2 not in known_primes:
        yield 2
    for index in xrange(1, cross_limit+1):
        if not sieve[index]:
            yield 2*(index)+1
            disable_sieve( index)
    for index in xrange(cross_limit+1, max_sieve+1):
        if not sieve[index]:
            yield 2*(index)+1
