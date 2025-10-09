'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

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


'''

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        current = dummy
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total = val1 + val2 + carry
            carry = total // 10
            current.next = ListNode(total % 10)
            current = current.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next





'''
we wlil approach htis way 

342
+465
-----
807


You start from the rightmost digit (units place), right? 2 + 5 = 7
Then 4 + 6 = 10 → write 0, carry 1 Then 3 + 4 + 1 (carry) = 8


## First Iteration (units place: 2 + 5)

>> val1 = l1.val if l1 else 0  # val1 = 2
>> val2 = l2.val if l2 else 0  # val2 = 5


>> total = val1 + val2 + carry  # total = 2 + 5 + 0 = 7
>> carry = total // 10          # carry = 7 // 10 = 0
>> current.next = ListNode(total % 10)  # current.next = ListNode(7)
>> current = current.next               # move current to the new node

# First digit of result: 7

## Sceond Iteration (tens place: 4 + 6)


>> val1 = 4
>> val2 = 6
>> total = 4 + 6 + 0 = 10
>> carry = 10 // 10 = 1
>> current.next = ListNode(10 % 10) = ListNode(0)
>> current = current.next


>> l1 = l1.next  # move to 3
>> l2 = l2.next  # move to 4


# Second digit of result: 0 
# Carry is now 1

## Third Iteration (hundreds place: 3 + 4 + carry)



val1 = 3
val2 = 4
total = 3 + 4 + 1 = 8
carry = 8 // 10 = 0
current.next = ListNode(8 % 10) = ListNode(8)
current = current.next



l1 = l1.next  # None
l2 = l2.next  # None


# Third dgiit of result: 8 
# No carry left

## Loop Ends

>> return dummy.next

# dummy.next points to the result list: 7 → 0 → 8
# This represents 807

and thenn fnila otuput 
Result Linked List: [7, 0, 8]



