




class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        if len(s) != len(t):
            return False
        
        str_map = {}
        position = 0
        mapped_str = ""
        
        while position < len(s):
            if s[position] not in str_map.values():
                str_map[t[position]] = s[position]
            
            position += 1
        
        for i in t:
            if i in str_map:
                mapped_str += str_map[i]

        return s == mapped_str
    
tests = []


tests.append({
    "input": {
        "s": "egg",
        "t": "add"
    },
    "output": True
})


tests.append({
    "input": {
        "s": "foo",
        "t": "bar"
    },
    "output": False
})


tests.append({
    "input": {
        "s": "paper",
        "t": "title"
    },
    "output": True
})

tests.append({
    "input": {
        "s": "bbbaaaba",
        "t": "aaabbbba"
    },
    "output": False
})


tests.append({
    "input": {
        "s": "",
        "t": ""
    },
    "output": True
})

tests.append({
    "input": {
        "s": "awdfds",
        "t": "dadwadwdawd"
    },
    "output": False
})





for test in tests:
    #print(Solution().isIsomorphic(**test["input"]))
    print(Solution().isIsomorphic(**test["input"]) == test["output"])