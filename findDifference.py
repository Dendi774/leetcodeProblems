




class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        for letter in t:
            if t.count(letter) >  s.count(letter):
                return letter



tests = []


tests.append({
    "input": {
        "s": "abcd",
        "t": "abcde"
    },
    "output": "e"
})

tests.append({
    "input": {
        "s": "",
        "t": "y"
    },
    "output": "y"
})


tests.append({
    "input": {
        "s": "a",
        "t": "aa"
    },
    "output": "a"
})

for test in tests:
    print(Solution().findTheDifference(**test["input"]) == test["output"])