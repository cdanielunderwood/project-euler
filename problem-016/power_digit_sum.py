from functools import reduce

# Problem 16
# 2^15 = 32768 and the sum of its digits is 3+2+7+6+8=26.
# What is the sum of the digits of the number ?

class PowerDigitSum:

    def __init__(self):
        pass

    def sum_digits_base_2(self,power):        
        print(f'power={power}')
        print(f'2**power={2**power}')
        return reduce(lambda x, y: x+y, map(int, str(2**power))) 
    