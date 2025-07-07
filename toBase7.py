




class Solution:
    def convertToBase7(self, num: int) -> str:
        ans = ""
        is_neg = False
        
        if num < 0:
            num *= -1
            is_neg = True
            
        while num > 0:
            ans += str(num%7)
            num = num//7
        
        if is_neg:
            ans += "-"
            
        return ans[::-1]
    
    

tests = []


tests.append({
    "input": {
        "num": 100
    },
    "output": "202"
})


tests.append({
    "input": {
        "num": -7
    },
    "output": "-10"
})

tests.append({
    "input": {
        "num": 7
    },
    "output": "10"
})


for test in tests:
    print(Solution().convertToBase7(**test["input"]) == test["output"])