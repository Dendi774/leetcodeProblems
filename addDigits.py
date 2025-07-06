




class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        
        prev_sum = num
        curr_sum = 0 
         
        while len(str(prev_sum)) > 1:
            for i in list(str(prev_sum)):
                curr_sum += int(i)
                
            prev_sum = (prev_sum * 0) + curr_sum
            curr_sum = 0
        
        
        return prev_sum
    
    
tests = []

tests.append({
    "input": {
        "num": 38
    },
    "output": 2 
})


tests.append({
    "input": {
        "num": 0
    },
    "output": 0
})


tests.append({
    "input": {
        "num": 123
    },
    "output": 6
})


tests.append({
    "input": {
        "num": 42069
    },
    "output": 3
})




for test in tests:
    print(Solution().addDigits(**test["input"]) == test["output"])