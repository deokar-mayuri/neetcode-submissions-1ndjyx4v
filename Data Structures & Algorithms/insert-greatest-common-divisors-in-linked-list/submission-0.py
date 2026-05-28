# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def findDiv(prevVal, nextVal):
            minVal = min(prevVal, nextVal)
            for i in reversed(range(1, minVal + 1)):
                if prevVal % i == 0 and nextVal % i == 0:
                    return i
        curr = head
        while curr.next:
            prevVal, nextVal = curr.val, curr.next.val
            div = findDiv(prevVal, nextVal)
            temp = ListNode(div)
            temp.next = curr.next
            curr.next = temp
            curr = curr.next.next
        return head