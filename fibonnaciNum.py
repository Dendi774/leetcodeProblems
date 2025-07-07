



class Solution:
    def fib(self, n):
        if n == 1 or n == 2:
            return 1
        else:
            return self.fib(n-2) + self.fib(n-1)


    def fib_bottomUp(self, n):
        memo = [None for i in range(n)]
        
        memo[0], memo[1] = 1, 1
        curr_index = 2

        while memo[n-1] == None:
            memo[curr_index] = memo[curr_index-1] + memo[curr_index-2]
            curr_index += 1
        
        return memo[n-1]

#print(Solution().fib(40))
print(Solution().fib_bottomUp(45))