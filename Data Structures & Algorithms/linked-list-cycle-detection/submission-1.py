# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        #slow and fast pointer technique:
        slow, fast = head, head # both pointers start in the same position 
        #slow moves one nodes while fast moves 2 nodes

        while fast and fast.next: #make sure the next 2 nodes are not null
            slow = slow.next
            fast = fast.next.next
            if slow == fast: #once the 2 pointers meet a cycle is confirmed
                return True
        return False #if NULL is ever reach it is automatically not a cycle 