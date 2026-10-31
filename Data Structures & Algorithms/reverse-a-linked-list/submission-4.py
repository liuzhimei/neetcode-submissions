# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # # no need to worry about the val in ListNode, just treat head as the first ListNode object
        # # ------ Method 1: iteratively, T: O(n), S: O(1) -------
        # # use two pointer and reverse each node
        # prev, curr = None, head
        # while curr:
        #     nxt = curr.next
        #     curr.next = prev
        #     prev = curr
        #     curr = nxt
        # return prev # last prev will be the new head for the reversed Linked list

        # --------- Method 2: recursively, T: O(n), S: O(1) --------
        # base case
        if not head:
            return None
        # induction step
        NewHead = head
        if head.next:
            NewHead = self.reverseList(head.next)
            head.next.next = head
        head.next = None
        return NewHead



