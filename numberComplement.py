




class Solution:
    def findComplement(self, num: int) -> int:
        bin = list(self.dec_to_bin(num))
        
        for i in range(len(bin)):
            if bin[i] == "1":
                bin[i] = "0"
            elif bin[i] == "0":
                bin[i] = "1"
        return self.bin_to_dec(bin) 

    def dec_to_bin(self, num):
        binary = ""
        while num > 0:
            binary += str(num%2)
            num = num // 2
        
        return binary[::-1]
    
    def bin_to_dec(self, bin):
        expo = len(bin)-1
        
        for i in range(len(bin)):
            bin[i] = int(bin[i]) * (2**expo)
            expo -= 1
        
        return sum(bin)
    
    
tests = []


tests.append({
    "input": {
        "num": 5
    },
    "output": 2
})

tests.append({
    "input": {
        "num": 1
    },
    "output": 0
})


tests.append({
    "input": {
        "num": 2
    },
    "output": 1
})


for test in tests:
    #print(Solution().findComplement(**test["input"]))
    print(Solution().findComplement(**test["input"]) == test["output"])