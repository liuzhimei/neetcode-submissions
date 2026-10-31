# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        curr = head
        idx = 0
        seen = set()
        while curr:
            if curr in seen:
                return True
            # curr.val = idx
            seen.add(curr)

            curr = curr.next
            # idx += 1
        return False
