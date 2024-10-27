import math

class PythagoreanTriplet:

    def __init__(self):
        pass

    def is_pythagorean_triplet(self, a, b, c):
        return (a**2)+(b**2) == (c**2)
    
    def get_product_of_triplet(self, a, b, c):
        return a*b*c

    def find_special_sum_triplet(self, sum):
        candidates = [ n for n in range(1, int(sum/2)) ]
        for a in candidates:
            for b in [ n for n in candidates if n>a]:
                    for c in [n for n in candidates if n>a and n>b]:
                            #print(f'testing a={a},b={b},c={c}...a+b+c={a+b+c}')
                            if a+b+c==sum and self.is_pythagorean_triplet(a,b,c):
                                print(f'*********************found it! {a},{b},{c}')
                                return a*b*c