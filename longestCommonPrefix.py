class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        
        """ Finds the longest common prefix in a list of strings """
        
        if len(strs) == 0:
            return ""
        
        end_idx_cmn_pfx = -1
        for letter_index, letter in list(enumerate(min(strs, key=len))):
            for inner in strs:
                if inner[letter_index] != letter:
                    if end_idx_cmn_pfx==-1:
                        return ""
                    return strs[0][:end_idx_cmn_pfx+1]
            end_idx_cmn_pfx+=1
            
        if len(strs)==1 or len(min(strs,key=len))==1:
            return min(strs, key=len)

        
        return strs[0][:end_idx_cmn_pfx+1]
            


print(Solution().longestCommonPrefix(strs = ["a", "b"]))