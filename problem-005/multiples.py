class Multiples:
    def is_factor(self, i, n):
        return n%i==0

    def smallest_multiple(self, limit):
        # find the smallest multiple that is evenly divisible by each of the numbers from 1 to limit without a remainder

        n = limit
        while not all([self.is_factor(i,n) for i in range(2,limit)]):
            n += limit
        return n
        