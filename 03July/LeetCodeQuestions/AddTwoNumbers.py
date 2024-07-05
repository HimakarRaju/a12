"""
Name : HimakarRaju Gunda
Date : 03-07-2024
Trainer Name : Saynam

Description of program :
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def add_two_numbers(l1, l2):
    dummy = ListNode()  # Dummy node to simplify handling of result list
    current = dummy  # Pointer to traverse the result list
    carry = 0  # Initialize carry to 0

    while l1 or l2 or carry:
        # Calculate sum of current digits and carry
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0
        sum_digits = val1 + val2 + carry

        # Update carry for next calculation
        carry = sum_digits // 10

        # Create new node for result list
        current.next = ListNode(sum_digits % 10)
        current = current.next

        # Move to next nodes in both lists if they exist
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None

    return dummy.next  # Return the next of dummy node, which is the head of result list


l1 = [2, 4, 3]
l2 = [5, 6, 4]

l3 = [0]
l4 = [0]

l5 = [9, 9, 9, 9, 9, 9, 9]
l6 = [9, 9, 9, 9]

print(add_two_numbers(l1, l2))
print(add_two_numbers(l3, l4))
print(add_two_numbers(l5, l6))
