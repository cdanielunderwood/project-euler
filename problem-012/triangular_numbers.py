class TriangularNumber:

    def __init__(self):
        pass
    
    def sum_triangular_number(self, n):
        return sum([n for n in range(1,n+1)])

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
    
    def get_divisors(self, n):        
        divisors = set()
        for i in range(1,int(n**0.5)+1):
            if n%i==0:
                divisors.add(i)
                divisors.add(n // i)
        return sorted(divisors)
                
    def find_first_triangular_number_by_number_of_divisors(self, count):
        triangular_numbers = [ [1, 1, [1], 1] ] #[ base number, triangular number, divisors, num of divisors]
        
        while triangular_numbers[-1][3] < count:
            next_base = triangular_numbers[-1][0] + 1
            next_tn =  self.sum_triangular_number(next_base)
            divisors = self.get_divisors(next_tn)
            triangular_numbers.append([next_base, next_tn, divisors, len(divisors)])
        return triangular_numbers[-1]
    