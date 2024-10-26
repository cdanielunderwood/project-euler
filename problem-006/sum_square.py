class SumSquares:

    def sum_squares(self, limit):
        return sum([i**2 for i in range(1,limit+1)])

    def square_sums(self, limit):
        return sum(range(1,limit+1))**2

    def square_sum_diff(self, limit):
        return self.square_sums(limit) - self.sum_squares(limit)