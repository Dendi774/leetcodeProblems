



class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """


        """ Messy and Inefficient Algorithm """
        cls_paren_index = 0
        
        
        while True:
            if cls_paren_index==len(s):
                return False
            
            elif s[cls_paren_index]==")" or s[cls_paren_index]=="]" or s[cls_paren_index]=="}":
                if s[cls_paren_index-1]+s[cls_paren_index]=="()" or s[cls_paren_index-1]+s[cls_paren_index]=="{}" or s[cls_paren_index-1]+s[cls_paren_index]=="[]":
                    s="".join(letter[1] for letter in list(enumerate(s)) if letter[0]!=cls_paren_index and letter[0]!=cls_paren_index-1)
                    if len(s)==0:
                        return True
                    cls_paren_index=0
                    continue
                return False
            cls_paren_index+=1
                    
        
        
        
print(Solution().isValid(s = "(("))
                
                    
                
        