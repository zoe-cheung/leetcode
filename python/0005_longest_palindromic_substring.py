""" Longest Palindromic Substring

LEVEL: Medium 

Given a string s, return the longest palindromic substring in s.

Example 1:
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:
Input: s = "cbbd"
Output: "bb"
 

Constraints:
1 <= s.length <= 1000
s consist of only digits and English letters.
"""

class Solution:
    
    def expandAroundCenter(self, s: str, left: int, right: int) -> str:
        """
        Expands around the center to find the longest palindromic substring.
        
        Args:
        s (str): The input string.
        left (int): The starting left index for expansion.
        right (int): The starting right index for expansion.
        
        Returns:
        str: The longest palindromic substring found by expanding around the center.
        """
        while left >= 0 and right < len(s) and s[left] == s[right]:
            print(f"left={left} right={right}   s[l]={s[left]}   s[r]={s[right]}")
            left -= 1
            right += 1
        return s[left + 1:right]
    
    def longestPalindrome(self, s: str) -> str:

        longest_palindrome = ""
        
        # CASE 1: If given string is less than 2, then empty return 0 and n=1 return 1
        if len(s) < 2:
            return s
        
        # Loop through each character in the string and treat it as a center
        for i in range(len(s)):
            # Odd-length palindromes (single character center)
            odd_palindrome = self.expandAroundCenter(s, i, i)
            # Even-length palindromes (two character center)
            even_palindrome = self.expandAroundCenter(s, i, i + 1)
            
            # Get the longer palindrome between odd and even centered
            longer_palindrome = max(odd_palindrome, even_palindrome, key=len)
            
            # Update the longest palindrome found so far
            if len(longer_palindrome) > len(longest_palindrome):
                longest_palindrome = longer_palindrome
        
        return longest_palindrome


if __name__ == "__main__":
    # Instantiate the Solution class
    sol = Solution()

    # Example 1: Input string "babad"
    s1 = "babad"
    result1 = sol.longestPalindrome(s1)
    print(f"Longest palindromic substring in '{s1}' is: '{result1}'")

    # Example 2: Input string "cbbd"
    s2 = "cbbd"
    result2 = sol.longestPalindrome(s2)
    print(f"Longest palindromic substring in '{s2}' is: '{result2}'")

    # Example 3: Input string with a single character
    s3 = "a"
    result3 = sol.longestPalindrome(s3)
    print(f"Longest palindromic substring in '{s3}' is: '{result3}'")

    # Example 4: Input string "ac"
    s4 = "ac"
    result4 = sol.longestPalindrome(s4)
    print(f"Longest palindromic substring in '{s4}' is: '{result4}'")


    """
    Time Complexity: O(n^2)
    Spance Complexity: O(1)
    """