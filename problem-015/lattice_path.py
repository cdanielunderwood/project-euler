from functools import reduce

class LatticePath:

    def __init__(self):
        pass

    def find_paths(self, grid_size):
        return int(self.factorial(grid_size*2)/(self.factorial(grid_size)*self.factorial(grid_size)))

    def factorial(self, n):
        return reduce(lambda x, y: x*y, range(1,n+1))
