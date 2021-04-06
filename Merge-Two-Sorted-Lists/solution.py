# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

        output_ListNode = None

        while l1 is not None or l2 is not None:
            if l1 is None:
                node = ListNode(l2.val)
                l2 = l2.next
            elif l2 is None:
                node = ListNode(l1.val)
                l1 = l1.next
            elif l1.val <= l2.val:
                node = ListNode(l1.val)
                l1 = l1.next
            elif l1.val > l2.val:
                node = ListNode(l2.val)
                l2 = l2.next
                
            if output_ListNode is None:
                output_ListNode = node
            else:
                end = output_ListNode
                while (end.next):
                    end = end.next
                end.next = node

        return output_ListNode
