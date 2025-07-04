



class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        
        """
        next_index = 1
        pascal_row = [[1],[1,1]]
        
        
        if numRows == 2:
            return [1,1]
        else:
            curr_row = self.generate(numRows-1)
            
            for i in curr_row:
                for j in curr_row[next_index:]:
                    pascal_row.append([i+j])
                    next_index+=1
                    break
                
                if next_index == len(curr_row):
                    break
                
        return pascal_row
        """
        
        
        
        if numRows == 1:
            pascal_rows = [[1]]
        
        elif numRows == 2:
            pascal_rows = [[1], [1,1]]
        
        else:
            curr_row = 1 
            next_index = 1
            pascal_rows = [[1],[1,1]]
            row_to_be_added = [1]
            
            while len(pascal_rows) < numRows:
                for i in pascal_rows[curr_row]:
                    for j in pascal_rows[curr_row][next_index:]:
                        row_to_be_added.append(i+j)
                        next_index += 1
                        break
                    
                    if next_index == len(pascal_rows[curr_row]):
                        row_to_be_added.append(1)
                        pascal_rows.append(row_to_be_added)
                        curr_row += 1
                        next_index = 1
                        row_to_be_added = [1]
                        break
        
        return pascal_rows
    

tests = []



tests.append({
    "input": {
        "numRows": 5
    },
    "output": [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
})

tests.append({
    "input": {
        "numRows": 1
    },
    "output": [[1]]
})

tests.append({
    "input": {
        "numRows": 1
    },
    "output": [[1]]
})


#print(Solution().generate(tests[1]["input"]["numRows"]))



for test in tests:
    print(Solution().generate(**test["input"]) == test["output"])