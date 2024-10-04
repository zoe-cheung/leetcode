""" Add Two Numbers 

LEVEL: Medium 
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit. 
Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1: 
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:
Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
 
Constraints:
The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.
"""
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        # Initialize dummy head for position
        dummyHead = ListNode(0)
        # Initialize current node to dummy head
        curr = dummyHead
        # Initial carry value to 0
        carry = 0
        
        # Loop through both linked list until both list ends is reach and carry = 0
        while l1 != None or l2 != None or carry != 0:
            
            l1Val = l1.val if l1 else 0
            l2Val = l2.val if l2 else 0
            
            # Get the sum for column
            columnSum = l1Val + l2Val + carry
            
            # Get remainder for carryover
            carry = columnSum // 10
            
            # Create new node with value (sum mod 10) 
            newNode = ListNode(columnSum % 10)
            curr.next = newNode
            #print(f'mid dummyHead: ', dummyHead)
            curr = newNode
            #print(f'dummyHead: ', dummyHead)
            
            # More to the next position
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            
        return dummyHead.next

# Function to print the linked list
def printLinkedList(node: Optional[ListNode]) -> None:
    while node:
        print(node.val, end=' -> ' if node.next else '\n')
        node = node.next

if __name__ == "__main__":
    # Create first number (e.g., 342 as 2 -> 4 -> 3)
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)

    # Create second number (e.g., 465 as 5 -> 6 -> 4)
    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)

    # Instantiate solution and run addTwoNumbers
    solution = Solution()
    result = solution.addTwoNumbers(l1, l2)

    # Print the result as a list
    print("The sum of the two numbers represented by the linked lists is: ")
    printLinkedList(result)