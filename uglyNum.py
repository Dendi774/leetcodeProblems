




class Solution:
    def isUgly(self, n: int) -> bool:
        factors = []
        
        if n < 1:
            return False
        
        while n%2==0:
            factors.append(2)
            n//=2
        
        i=3
        while i*i<=n:
            while n%i==0:
                factors.append(i)
                n//=i
            
            i += 2
            
        if n > 2:
            factors.append(n)
            
        
        if len([factor for factor in set(factors) if factor != 2 and factor != 3 and factor != 5 and factor != 1]) == 0:
            return True
        return False
    
    
tests = []


tests.append({
    "input": {
        "n": 6
    },
    "output": True
})


tests.append({
    "input": {
        "n": 1
    },
    "output": True
})


tests.append({
    "input": {
        "n": 14
    },
    "output": False
})


tests.append({
    "input": {
        "n": 8
    },
    "output": True
})


tests.append({
    "input": {
        "n": 25
    },
    "output": True
})


tests.append({
    "input": {
        "n": 905391974
    },
    "output": False
})


tests.append({
    "input": {
        "n": -2147483648
    },
    "output": False
})

tests.append({
    "input": {
        "n": 0
    },
    "output": False
})




for test in tests:
   # print(Solution().isUgly(**test["input"]))
    print(Solution().isUgly(**test["input"]) == test["output"])