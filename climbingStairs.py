import math


class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        # n=4
        """
            1+1+1+1
            2+2
            1+1+2
            2+1+1
            1+2+1
        """
        
        #n=5
        """
            1+1+1+1+1
            2+2+1
            1+2+2
            2+1+2
            1+1+1+2
            2+1+1+1
            1+2+1+1
            1+1+2+1
            
        """
        #n=6
        """
            1+1+1+1+1+1
            2+2+2
            1+1+1+1+2
            2+1+1+1+1
            1+2+1+1+1
            1+1+2+1+1
            1+1+1+2+1
            2+2+1+1
            1+1+2+2
            1+2+2+1
            1+2+1+2
            2+1+1+2
            2+1+2+1
        """
        
        #n=7
        """
            1+1+1+1+1+1+1
            2+2+2+1
            2+2+1+2 
            2+1+2+2
            1+2+2+2
            1+1+1+1+1+2
            1+1+1+1+2+1
            1+1+1+2+1+1
            1+1+2+1+1+1
            1+2+1+1+1+1
            2+1+1+1+1+1
        """
        
        
        num_of_steps = [1 for i in range(n)]
        num_of_Ways = 1
        
        if n==2:
            return n
        
        if n%2==0:
            num_of_Ways+=1
            
        for i in range(n):
            if num_of_steps.count(1) > 1:
                num_of_steps.remove(1)
                num_of_steps.remove(1)
            else:
                return int(num_of_Ways)
            
            num_of_steps.append(2)
            
            if sum(num_of_steps)==n:
                if num_of_steps.count(1)>1 and num_of_steps.count(2)>1:
                    if num_of_steps.count(1) < num_of_steps.count(2):
                        num_of_Ways += (math.factorial(len(num_of_steps))/(math.factorial(num_of_steps.count(1))*(math.factorial(len(num_of_steps)-num_of_steps.count(1)))))
                    elif num_of_steps.count(2) < num_of_steps.count(1):
                        num_of_Ways += (math.factorial(len(num_of_steps))/(math.factorial(num_of_steps.count(2))*(math.factorial(len(num_of_steps)-num_of_steps.count(2)))))
                    else:
                        num_of_Ways += (math.factorial(len(num_of_steps))/(math.factorial(num_of_steps.count(1))*(math.factorial(len(num_of_steps)-num_of_steps.count(1)))))
                elif num_of_steps.count(1)==1 or num_of_steps.count(2)==1:
                    num_of_Ways += (math.factorial(len(num_of_steps))/(math.factorial(1)*(math.factorial(len(num_of_steps)-1))))
        
        
print(Solution().climbStairs(n=45))