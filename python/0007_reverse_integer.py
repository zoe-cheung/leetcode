""" Reverse Integer

LEVEL: Medium 

Given a signed 32-bit integer x, return x with its digits reversed. 
If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Example 1:
Input: x = 123
Output: 321

Example 2:
Input: x = -123
Output: -321

Example 3:
Input: x = 120
Output: 21
 
Constraints:
-231 <= x <= 231 - 1
"""

class Solution:
    def reverse(self, x: int) -> int:

        # Define the boundaries for a 32-bit signed integer
        INT_MIN, INT_MAX = -2**31, 2**31 - 1

        # Determine the sign of the number and convert x to its absolute value
        sign = -1 if x < 0 else 1
        x = abs(x)

        # Reverse the digits by converting to string, reversing, and converting back to integer
        reversed_x = int(str(x)[::-1])

        # Apply the sign to the reversed number
        reversed_x *= sign

        # Check if the reversed number is within the 32-bit signed integer range
        if reversed_x < INT_MIN or reversed_x > INT_MAX:
            return 0
        
        return reversed_x


if __name__ == "__main__":
    sol = Solution()
    print(sol.reverse(123))    # Output: 321
    print(sol.reverse(-123))   # Output: -321
    print(sol.reverse(120))    # Output: 21
    print(sol.reverse(0))      # Output: 0

"""
Time Complexity: O(n)
Space Complexity: O(n)
"""