""" Two Sum 

Level: Easy 
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]
 
Constraints:
2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
 
Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
"""

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # Create empty hash map
        hashmap = {}
        
        for i in range(0, len(nums)):
            temp = target - nums[i]
            if (temp in hashmap):
                print(f'For target {target}, there is a pair ({nums[i]}, {temp}) at indices ({i}, {hashmap[temp]})')
                return i, hashmap[temp]
            hashmap[nums[i]] = i 

# Example to test the function
if __name__ == "__main__":
    solution = Solution()
    nums = [2, 7, 11, 15]
    target = 9
    result = solution.twoSum(nums, target)
    print(f'Indices of the numbers that sum to {target}: {result}')


""" Overall Time Complexity: O(n)
Best Case Time Complexity: O(1) if the solution is found immediately.
Worst Case Time Complexity: O(n) if we have to iterate through the entire list to find the pair or return no solution.
"""