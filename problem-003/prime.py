import math

class Prime:

   def get_max_prime_factor(self, n):
        
        p = 2
        while p*p <= n:
            if n%p==0:
                n//=p
            else:
                p+=1
        return n
    