# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        ## ------ Use hashset with space complexity O(n) --------
        # curr = head
        # idx = 0
        # seen = set()
        # while curr:
        #     if curr in seen:
        #         return True
        #     # curr.val = idx
        #     seen.add(curr) # can directly add node object into set

        #     curr = curr.next
        #     # idx += 1
        # return False

        # ----- advanced method with space complexity O(1) --------
        # Floyd's Tortoise & Hare
        # Idea of fast pointer and slow pointer: shift the slow pointer by 1 each time, while faster pointer by 2 each time. If a cycle exists, then the fast and slow pointer should meet 
        slow, fast = head, head
        while fast and fast.next: # while fast pointer and its next one are not null, otherwise if one of them reaches null, there is no cycle
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False



        
