



class Solution:
    def fib(self, n):
        if n == 1 or n == 2:
            return 1
        else:
            return self.fib(n-2) + self.fib(n-1)
    

print(Solution().fib(30))