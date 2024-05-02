# Q1: Detect cycle in linked list

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def has_cycle(head):
    if not head or not head.next:
        return False
    
    slow = head
    fast = head.next
    
    while slow != fast:
        if not fast or not fast.next:
            return False
        slow = slow.next
        fast = fast.next.next
    
    return True

# Example usage
# Create a linked list with a cycle
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = head.next  # Creating a cycle

# Detect cycle
print("Does the linked list have a cycle?", has_cycle(head))
