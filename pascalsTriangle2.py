



class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """

        numRows = rowIndex + 1

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
        
        return pascal_rows[rowIndex]





tests = []

tests.append({
    "input": {
        "rowIndex": 3
    },
    "output": [1,3,3,1]
})


tests.append({
    "input": {
        "rowIndex": 0
    },
    "output": [1]
})


tests.append({
    "input": {
        "rowIndex": 1
    },
    "output": [1,1]
})


for test in tests:
    print(Solution().getRow(**test["input"]) == test["output"])