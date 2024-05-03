# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def recurse(node):
            # Reach the end of linkedlist
            if (node == None): 
                return node, 0
            
            # Return the node and carry of next node
            next_node, carry = recurse(node.next) 
            # Perform multiplication for the current node
            carry, node.val = (node.val * 2 + carry) // 10, (node.val * 2 + carry) % 10
            return node, carry
        
        # Do the doubling in recursion
        node, carry = recurse(head)
        # Add a head node if carry > 0
        if carry > 0:
            dummy = ListNode(carry)
            dummy.next = node
            return dummy
        else:
            return node
