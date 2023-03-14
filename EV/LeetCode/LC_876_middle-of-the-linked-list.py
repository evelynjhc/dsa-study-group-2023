'''
    runtime: 24 ms Beats 96.11%
    memory: 13.8 MB Beats 92.96%
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        list_len = 1
        
        while curr.next:
            list_len += 1
            curr = curr.next
        for _ in range(list_len // 2):
            head = head.next
        
        return head

# reuse of the variables(curr, list_len) helped in memory usage