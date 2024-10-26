class Palindrome:

    def is_palindrome(self, n):
        return str(n)==str(n)[::-1]

    def max_palidrome_product(self, max_digits):
        limit = int(str(9)*max_digits)
        
        max_p = 0
        for i in range(limit,0,-1):
            for j in range(limit,0,-1):
                p = i*j
                if self.is_palindrome(p) and p>max_p:
                    max_p=p
        return max_p


