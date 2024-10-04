""" Zigzag Conversion

LEVEL: Medium 

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: 
(you may want to display this pattern in a fixed font for better legibility)
P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows: 
    string convert(string s, int numRows);

Example 1:
Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"

Example 2:
Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"

Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I

Example 3:
Input: s = "A", numRows = 1
Output: "A"
 
Constraints:
1 <= s.length <= 1000
s consists of English letters (lower-case and upper-case), ',' and '.'.
1 <= numRows <= 1000
"""

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # Edge case: if numRows is either 1 or greater than length of s, return the string as-is
        if numRows == 1 or numRows >= len(s):
            return s

        # Create a list to store strings for each row and checkpoint
        rows = [''] * numRows
        cur_row = 0
        going_down = False

        # Iterate through the string and place characters in the right row
        for char in s:
            rows[cur_row] += char
            # Change direction when top or bottom row reach
            if cur_row == 0 or cur_row == numRows - 1:
                going_down = not going_down
            cur_row += 1 if going_down else -1

        # Concatenate all rows to get zigzagged string
        return ''.join(rows)

if __name__ == "__main__":

    sol = Solution()
    print(sol.convert("PAYPALISHIRING", 3))  # Output: "PAHNAPLSIIGYIR"
    print(sol.convert("PAYPALISHIRING", 4))  # Output: "PINALSIGYAHRPI"
    print(sol.convert("A", 1))               # Output: "A"

