class Multiples:

    def isMultipleOf3(self, integer):
        return integer%3==0

    def isMultipleOf5(self, integer):
        return integer%5==0

    def sumMultiplesOf3And5(self, integer):
        return sum([n for n in range(integer) if self.isMultipleOf3(n) or self.isMultipleOf5(n)]) 
     
    