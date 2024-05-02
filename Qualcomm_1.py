# Q1: Detect cycle in linked list
# Ans:
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

# Q2: Insert a node at last using doubly linked.
# Ans:
class ListNode:
    def __init__(self, val=0, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

def insert_at_end(head, val):
    new_node = ListNode(val)
    if not head:
        return new_node
    current = head
    while current.next:
        current = current.next
    current.next = new_node
    new_node.prev = current
    return head

head = ListNode(1)
head.next = ListNode(2, prev=head)
head.next.next = ListNode(3, prev=head.next)

print("Doubly linked list before insertion:")
current = head
while current:
    print(current.val)
    current = current.next

# Insert a node at the end
head = insert_at_end(head, 4)

print("\nDoubly linked list after insertion:")
current = head
while current:
    print(current.val)
    current = current.next
    
# Q3: WAP for factorial
# Ans:
def factorial(n):
    if n==0:
        return 1
    return n*factorial(n-1)
    
ip=5
op= factorial(ip) 
print(op)

# Q4:









