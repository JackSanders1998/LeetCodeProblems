# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1_sum = 0
        l1_exponent = 0
        l2_sum = 0
        l2_exponent = 0
        while l1 is not None:
            l1_sum += l1.val * (10**l1_exponent)
            l1_exponent += 1
            l1 = l1.next
        while l2 is not None:
            l2_sum += l2.val * (10**l2_exponent)
            l2_exponent += 1
            l2 = l2.next
        total_sum = l1_sum + l2_sum
        if total_sum == 0:
            return ListNode(0)
        output = None
        while total_sum != 0:
            node = ListNode(total_sum % 10)
            total_sum = total_sum // 10
            
            if output is None:
                output = node
            else: 
                last = output
                while (last.next):
                    last = last.next
                last.next = node
        return output


