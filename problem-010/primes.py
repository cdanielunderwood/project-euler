class Prime:
    def get_nth_prime(self, n):
        primes = []
        counter=1
        while n>len(primes):
            primes = self.get_primes(n*counter)
            counter += 1
        return primes[n-1]
    
    def get_primes(self, limit):
        prime_sieve = self.get_prime_sieve(limit)
        return [ p for p in range(2,limit+1) if prime_sieve[p] ]

    def get_prime_sieve(self, limit):
        prime = [ True for _ in range(limit+1) ]
        p = 2

        while p*p <= limit:
            if prime[p]:
                # mark multiples of prime as not prime
                for i in range(p*p, limit+1, p):
                    prime[i] = False
            p+=1
        return prime

    def sum_primes(self, limit):
        return sum(self.get_primes(limit))