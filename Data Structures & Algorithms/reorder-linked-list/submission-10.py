# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        # ---- Method: slow and fast pointer -----
        slow, fast = head, head
        while fast and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        # if fast.next:
        #     fast = fast.next # last one in the list if length is even
        
        # break the list into two halves and reverse the second half of the list
        # Note: when reversing a linked list, start with prev=None, curr=head
        prev = None
        curr = slow.next
        slow.next = None # break the list after slow pointer
        while curr:
            nxt = curr.next
            curr.next = prev # reverse edge order between prev and curr
            prev = curr # update prev
            curr = nxt # update curr
        
        pointer1 = head
        pointer2 = prev # get the head for the reversed second half
        while pointer2:
            nxt1 = pointer1.next
            nxt2 = pointer2.next
            pointer1.next = pointer2
            pointer2.next = nxt1
            pointer1 = nxt1
            pointer2 = nxt2


        # return head



