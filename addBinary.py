

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        
        
        carry = 0
        sum = ""
    
        
        if len(a) > len(b):
            b = b[::-1]
            for i in range(len(a)-len(b)):
                b+="0"
            a = a[::-1]
            
        elif len(a) < len(b):
            a= a[::-1]
            for i in range(len(b)-len(a)):
                a+="0"
                print(a)
            b = b[::-1]
            


        else:
            a = a[::-1]
            b = b[::-1]
            
        
        print(f"\n{a}, {b}")
    
        for digit in enumerate(a):
            print(carry)
            if int(digit[1]) + int(b[digit[0]]) + carry == 3:
                carry = 1
                sum += "1"
            elif int(digit[1]) + int(b[digit[0]]) + carry == 2:
                carry = 1
                sum += "0"
            else:
                sum += str(int(digit[1]) + int(b[digit[0]]) + carry)
                carry = 0
                
        if carry > 0:
            sum+=str(carry)
        
        return sum[::-1]
        
        
        

print(Solution().addBinary(a = "11", b = "1"))
print(Solution().addBinary(a = "1010", b = "1011"))
print(Solution().addBinary(a = "100", b = "110010"))