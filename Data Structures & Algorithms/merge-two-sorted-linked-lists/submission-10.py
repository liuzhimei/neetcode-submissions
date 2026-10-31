# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        pointer1 = list1
        pointer2 = list2
        if not list1 and list2:
            return list2
        elif list1 and not list2:
            return list1
        elif not list1 and not list2:
            return None
        # initialise output linked list
        if pointer1.val < pointer2.val:
            head = pointer1
            tail = pointer1
            pointer1 = pointer1.next
        else:
            head = pointer2
            tail = pointer2
            pointer2 = pointer2.next
        while pointer1 or pointer2:
            if pointer1 is None:
                tail.next = pointer2
                tail = tail.next # update tail in output
                pointer2 = pointer2.next
            elif pointer2 is None:
                tail.next = pointer1
                tail = tail.next
                pointer1 = pointer1.next
            else:
                if pointer1.val < pointer2.val:
                    tail.next = pointer1
                    tail = tail.next
                    pointer1 = pointer1.next
                else:
                    tail.next = pointer2
                    tail = tail.next
                    pointer2 = pointer2.next
        
        return head
                
