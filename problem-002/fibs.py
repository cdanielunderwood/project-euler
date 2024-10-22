class Fibs:

    def isEven(self, integer):
        return integer%2==0

    def getFibsUpTo(self, n):
        fibs = [1,2]
        while max(fibs)<n:
            fibs.append(fibs[-2]+fibs[-1])
        print(f'getFibsUpTo({n})={fibs[:-1]}')
        return fibs[:-1]
    
    def sumEvenFibsUpTo(self, n):
        sumOfEvens = sum([x for x in self.getFibsUpTo(n) if self.isEven(x)])
        print(sumOfEvens)
        return sumOfEvens