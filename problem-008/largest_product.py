from functools import reduce

class LargestProduct:

    def __init__(self):
        self.series=""

    def append_series(self, series):
        self.series += series

    def get_series(self):
        return self.series

    def get_slices(self, size):
        return [self.series[i:i+size] for i in range(len(self.series)-size)]

    def get_product(self, slice):
        return reduce(lambda x, y: int(x)*int(y), slice)


    def find_largest_product(self, size):
        products = []
        for slice in self.get_slices(size):
            products.append(self.get_product(slice))
        return max(products)
