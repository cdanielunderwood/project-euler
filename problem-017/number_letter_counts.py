class NumberLetterCounts:

    def __init__(self):
        self.ones = {
            0: '', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 
            5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine',
            10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 
            15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen'
        }

        self.tens = {
            2: 'twenty', 3: 'thirty', 4: 'forty', 5: 'fifty', 6: 'sixty',
            7: 'seventy', 8: 'eighty', 9: 'ninety'
        }

    
    def num_to_words(self, n):
        if (n<20):
            return self.ones[n]
        elif (n<100):
            return self.tens[n // 10] + self.num_to_words(n%10)
        elif (n<1000):
            if (n%100>0): 
                return self.ones[n // 100] + 'hundredand' + self.num_to_words(n%100) # add the british 'and' if there is a remainder
            else:
                return self.ones[n // 100] + 'hundred' # no remainder 
        elif (n<10000):
            if (n%1000>0):
                return self.ones[n // 1000] + 'thousandand' + self.num_to_words(n%1000) # add the british 'and' if there is a remainder
            else:
                return self.ones[n // 1000] + 'thousand' # no remainder 
        else:
            return ''

    def count_letters_in_number(self,n):
        print(f'{n} is {self.num_to_words(n)} with {len(self.num_to_words(n))} letters.')
        return len(self.num_to_words(n))
    
