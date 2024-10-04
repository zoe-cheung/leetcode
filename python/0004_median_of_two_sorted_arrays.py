""" Median of Two Sorted Arrays

LEVEL: Hard 

Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
The overall run time complexity should be O(log (m+n)).

Example 1:
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Example 2:
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

Constraints:
nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106
"""
from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Ensure nums1 is the smaller array to optimize the binary search
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        m, n = len(nums1), len(nums2)
        total_len = m + n
        half_len = (total_len +1) // 2 # This will help handle odd and even lengths
        print(f"\nhalf length: {half_len}")
        
        # Binary search on the smaller array 
        # This ensures an efficient search with time complexity O(log(min(m, n)))
        low, high = 0, m
        while low <= high:
            i = (low + high) // 2  # Partition in nums1
            j = half_len - i  # Partition in nums2
            
            # Edge cases: 
            nums1_left_max = float('-inf') if i == 0 else nums1[i - 1]
            nums1_right_min = float('inf') if i == m else nums1[i]
            nums2_left_max = float('-inf') if j == 0 else nums2[j - 1]
            nums2_right_min = float('inf') if j == n else nums2[j]

            
            print(f"\nlow={low}   high={high}")
            print(f"i={i}   j={j}")
            print(f"nums1_left_max={nums1_left_max}   nums1_right_min={nums1_right_min}")
            print(f"nums2_left_max={nums2_left_max}   nums2_right_min={nums2_right_min}")
            print(f"{nums1_left_max}<={nums2_right_min}   {nums2_left_max}<={nums1_right_min}")
            print(f"{nums1_left_max}>{nums2_right_min}")
            print(f"total_len={total_len}; {total_len % 2}")
            
            # Check if we have found the correct partition
            if nums1_left_max <= nums2_right_min and nums2_left_max <= nums1_right_min:
                # If total length is odd, return the max of the left half
                if total_len % 2 == 1:
                    return max(nums1_left_max, nums2_left_max)
                # If total length is even, return the average of the two middle values
                return (max(nums1_left_max, nums2_left_max) + min(nums1_right_min, nums2_right_min)) / 2
            
            # If nums1 partition is too far right, move left
            elif nums1_left_max > nums2_right_min:
                high = i - 1
            # If nums1 partition is too far left, move right
            else:
                low = i + 1
        
        # Edge case: in case something went wrong
        raise ValueError("Input arrays are not sorted or invalid.")

# TIME COMPLEXITY: O(log(min(m, n)))

if __name__ == "__main__":

    # Example 1:
    nums1 = [1, 3]
    nums2 = [2]
    output1 = Solution().findMedianSortedArrays(nums1, nums2)
    print(f"Median of arrays {nums1} and {nums2} is: {output1}")

    # Example 2:
    nums1 = [1, 2]
    nums2 = [3, 4]
    output2 = Solution().findMedianSortedArrays(nums1, nums2)
    print(f"Median of arrays {nums1} and {nums2} is: {output2}")

    # Example 2:
    nums1 = [1, 2, 5]
    nums2 = [3, 4]
    output2 = Solution().findMedianSortedArrays(nums1, nums2)
    print(f"Median of arrays {nums1} and {nums2} is: {output2}")