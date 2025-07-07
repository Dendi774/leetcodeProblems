




class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        import math

        if n > 0 and int(math.log(n, 3)) == math.log(n, 3):
            return True
        return False


tests = []


tests.append({
    "input": {
        "n": 27
    },
    "output": True
})


tests.append({
    "input": {
        "n": 0
    },
    "output": False
})


tests.append({
    "input": {
        "n": -1
    },
    "output": False
})


tests.append({
    "input": {
        "n": 9
    },
    "output": True
})


tests.append({
    "input": {
        "n": 81
    },
    "output": True
})


tests.append({
    "input": {
        "n": 729
    },
    "output": True
})

tests.append({
    "input": {
        "n": 243
    },
    "output": True
})





#print(Solution().isPowerOfThree(**tests[len(tests)-1]["input"]))
#print(Solution().isPowerOfThree(**tests[len(tests)-2]["input"]))
for test in tests:
    print(Solution().isPowerOfThree(**test["input"]) == test["output"])
    