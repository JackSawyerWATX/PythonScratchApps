


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def create_linked_list(elements):
    head = None
    prev = None
    for value in elements:
        node = Node(value)
        if prev:
            prev.next = node
        else:
            head = node
        prev = node
    return head

def reverse_linked_list(head):
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev

def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=' -> ')
        current = current.next
    print("None")

# Create the linked list
elements = [3, 4, 5, 6, 7]
head = create_linked_list(elements)

# Print the original linked list
print("Original Linked List:")
print_linked_list(head)

# Reverse the linked list
reversed_head = reverse_linked_list(head)

# Print the reversed linked list
print("Reversed Linked List:")
print_linked_list(reversed_head)
