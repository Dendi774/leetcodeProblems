




class Solution:
    def canWinNim(self, n: int) -> bool:
        pass




tests = []

tests.append({
    "input": {
        "n": 4
    },
    "output": False
})


tests.append({
    "input": {
        "n": 1
    },
    "output": True
})


tests.append({
    "input": {
        "n": 2
    },
    "output": True
})


tests.append({
    "input": {
        "n": 5
    },
    "output": True
})


tests.append({
    "input": {
        "n": 6
    },
    "output": True
})

tests.append({
    "input": {
        "n": 7
    },
    "output": True
})


tests.append({
    "input": {
        "n": 8
    },
    "output": True
})

tests.append({
    "input": {
        "n": 9
    },
    "output": True
})

tests.append({
    "input": {
        "n": 10
    },
    "output": True
})


for test in tests:
    print(Solution().canWinNim(**test["input"]) == test["output"])