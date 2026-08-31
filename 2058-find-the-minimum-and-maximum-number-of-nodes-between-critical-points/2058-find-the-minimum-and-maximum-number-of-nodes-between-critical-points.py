# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        if not head or not head.next or not head.next.next:
            return [-1, -1]

        min_dist=float('inf')
        first_cp_idx=-1
        prev_cp_idx=-1

        prev=head
        curr=head.next
        idx=1

        while curr.next:
            nxt=curr.next

            is_maxima=curr.val > prev.val and curr.val>nxt.val
            is_minima=curr.val<prev.val and curr.val<nxt.val

            if is_maxima or is_minima:
                if first_cp_idx==-1:
                    first_cp_idx=idx
                else:
                    min_dist=min(min_dist,idx-prev_cp_idx)
                prev_cp_idx=idx

            prev=curr
            curr=nxt
            idx+=1
        if first_cp_idx==prev_cp_idx:
            return [-1,-1]
        max_dist=prev_cp_idx-first_cp_idx
        return [min_dist,max_dist]

        
