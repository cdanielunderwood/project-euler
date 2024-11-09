class Collatz:

    def __init__(self):
        pass

    def get_max_sequence_length(self, limit):
        limits = [0]
        for i in range(1,limit):
            limits.append(len(self.get_sequence(i)))
        return limits.index(max(limits))


    def get_sequence(self, start):
        sequence = [start]
        while sequence[-1]>1:
            if self.is_even(sequence[-1]):
                sequence.append(self.next_even(sequence[-1]))
            else:
                sequence.append(self.next_odd(sequence[-1]))
        #print(f'Collatz sequence starting with {start} is {sequence}.')
        return sequence

    def is_even(self, num):
        return num%2==0

    def next_even(self,num):
        return int(num/2)

    def next_odd(self,num):
        return int((3*num)+1)
