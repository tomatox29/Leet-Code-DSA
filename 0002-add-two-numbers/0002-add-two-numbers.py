# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # dummy = ListNode()
        # current = dummy 
        # carry = 0 
        # while l1 or l2 or carry:
        #     x = l1.val if l1 else 0 
        #     y = l2.val if l2 else 0

        #     total = x + y + carry 
        #     digit = total % 10 
        #     carry = total // 10 
        #     current.next=ListNode(digit)
        #     current = current.next

        #     if l1 :
        #         l1=l1.next
        #     if l2:
        #         l2= l2.next 

        # return dummy.next
        

    #second approach converting both linked lists as a srting then reversing it and and then add and then reversing the total again to get the orginal form than add digit by digit of total in the linked list  
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        num1 = ""
        while l1:
            num1 += str(l1.val)
            l1 = l1.next

        num2 = ""
        while l2:
            num2 += str(l2.val)
            l2 = l2.next

        num1 = int(num1[::-1])
        num2 = int(num2[::-1])

        total = str(num1 + num2)[::-1]

        dummy = ListNode()
        current = dummy

        for digit in total:
            current.next = ListNode(int(digit))
            current = current.next

        return dummy.next