




class Solution:
    def isHappy(self, n: int) -> bool:
        n_digits = list(str(n))
        cycles = []
        
        while True:
            n = 0
            for digit in n_digits:
                n += int(digit)**2
            
            if n == 1:
                return True
            elif n in cycles:
                return False

            cycles.append(n)
            n_digits = list(str(n))
            
tests = []


tests.append({
    "input": {
        "n": 19
    },
    "output": True
})


tests.append({
    "input": {
        "n": 2
    },
    "output": False
})


tests.append({
    "input": {
        "n": 3
    },
    "output": False
})


tests.append({
    "input": {
        "n": 25
    },
    "output": False
})



tests.append({
    "input": {
        "n": 7
    },
    "output": True
})


for test in tests:
    print(Solution().isHappy(**test["input"]) == test["output"])