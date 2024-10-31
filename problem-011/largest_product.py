from functools import reduce

class LargestProduct:


    def get_product(self, slice):
        return int(reduce(lambda x, y: int(x)*int(y), slice))

    def get_horizontal_slices(self, grid, size):
        slices = []
        for row in grid:
            for i in range(len(row)-size+1):
                slices.append(row[i:i+size])
        return slices

    def get_vertical_slices(self, grid, size):
        return self.get_horizontal_slices(self.rotate_grid(grid), size)
    
    def rotate_grid(self, grid):
        return list(zip(*reversed(grid)))

    def get_upper_diagonal_slices(self, grid, size):
        slices = []
        for i in range(size-1,len(grid)):
            for j in range(len(grid[i])-size+1):
                slices.append([grid[i-k][j+k] for k in range(size)])
        return slices

    def get_lower_diagonal_slices(self, grid, size):
        slices = []
        for i in range(len(grid)-size+1):
            for j in range(len(grid[i])-size+1):
                slices.append([grid[i+k][j+k] for k in range(size)])
        return slices

    def get_slices(self, grid, size):
        slices = self.get_horizontal_slices(grid, size)
        slices += self.get_vertical_slices(grid, size)
        slices += self.get_lower_diagonal_slices(grid, size)
        slices += self.get_upper_diagonal_slices(grid, size)
        return slices

    def find_largest_product(self, grid, size):
        products = []
        for slice in self.get_slices(grid, size):
            products.append(self.get_product(slice))
        return max(products)