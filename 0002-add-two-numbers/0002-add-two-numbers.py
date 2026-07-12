# Solution 1: Convert to Number (Python)
# Logic:
# * Traverse both linked lists.
# * Store digits as strings.
# * Reverse and convert to integers.
# * Add the numbers.
# * Reverse the sum.
# * Create a new linked list from the digits.
# Time: O(n + m)
# Space: O(n + m)

# Note: Easy Python solution, but not the standard interview approach.

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


# Solution 2: Digit-by-Digit Addition
# Logic:
# * Traverse both linked lists together.
# * Add corresponding digits and carry.
# * Store sum % 10 in a new node.
# * Update carry = sum // 10.
# * Continue until both lists and carry are finished.
# Time: O(n + m)
# Space: O(max(n, m))
# Note: Standard interview solution. Works in all languages.

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy 
        carry = 0 
        while l1 or l2 or carry:
            x = l1.val if l1 else 0 
            y = l2.val if l2 else 0

            total = x + y + carry 
            digit = total % 10 
            carry = total // 10 
            current.next=ListNode(digit)
            current = current.next

            if l1 :
                l1=l1.next
            if l2:
                l2= l2.next 

        return dummy.next

