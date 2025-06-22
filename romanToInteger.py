



class Solution1:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        """ Inneficient Solution, lots of slicing and unnecessary enumerate() """
        
        roman_nums = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        
        special_cases = {
            "IV": 4,
            "IX": 9,
            "XL": 40,
            "XC": 90,
            "CD": 400,
            "CM": 900
        }
        
        output_int = 0
        start_index = 0
        
        while True:
            for roman_index, roman_num in list(enumerate(s[start_index:])):
                if roman_index<len(list(enumerate(s[start_index:])))-1:
                    if roman_num+s[start_index:][roman_index+1] in special_cases.keys():
                        output_int += special_cases[roman_num+s[start_index:][roman_index+1]]
                        start_index = start_index+roman_index+2
                        break

                output_int += roman_nums[roman_num]

                if roman_index == len(s[start_index:])-1:
                    return output_int
                

            if len(s[start_index:])==0:
                return output_int


class Solution2:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        """ More efficient algorithm, where we only loop through the string once """
        
        roman_nums = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        
        special_cases = {
            "IV": 4,
            "IX": 9,
            "XL": 40,
            "XC": 90,
            "CD": 400,
            "CM": 900
        }
        
        output_int = 0
        start_index = 0
        
        
        for i in s:
            if start_index<len(s)-1 and s[start_index]+s[start_index+1] in special_cases.keys():
                output_int+=special_cases[s[start_index]+s[start_index+1]]
                start_index+=2
                continue
            elif start_index > len(s)-1:
                return output_int
            
            output_int += roman_nums[s[start_index]]
            start_index+=1
        
        return output_int

                

print(Solution2().romanToInt(s = "III"))