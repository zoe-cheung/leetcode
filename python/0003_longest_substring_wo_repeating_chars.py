""" Longest Substring Without Repeating Characters

Level: Medium 
Given a string s, find the length of the longest substring without repeating characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 
Constraints:
0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
"""

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        # initial dict to store last index of every character
        last_idx = {}
        # initialize the maximum length
        max_len = 0
        # starting index of current to calculate max_len
        start_idx = 0

        # Loop through the given string
        for i in range(0, len(s)):

            # Find the last index of string[i]
            # Update start_idx = maximum of current value of start_idx and last_idx + 1
            if s[i] in last_idx:
                start_idx = max(start_idx, last_idx[s[i]] + 1)

            # Update max length
            max_len = max(max_len, i-start_idx + 1)
                    
            # Update last index
            last_idx[s[i]] = i
            # Checkpoint: print(f"last_idx: {last_idx}")


        return max_len

if __name__ == "__main__":
    # Test cases
    solution = Solution()

    # Example 1
    s = "abcabcbb"
    print(solution.lengthOfLongestSubstring(s))  # Output: 3

    # Example 2
    s = "bbbbb"
    print(solution.lengthOfLongestSubstring(s))  # Output: 1

    # Example 3
    s = "pwwkew"
    print(solution.lengthOfLongestSubstring(s))  # Output: 3

    # Edge case with an empty string
    s = ""
    print(solution.lengthOfLongestSubstring(s))  # Output: 0