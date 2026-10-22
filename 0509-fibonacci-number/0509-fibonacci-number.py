class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        lastdigit = self.fib(n - 1)
        slastdigit = self.fib(n - 2)
        return lastdigit + slastdigit
    

        