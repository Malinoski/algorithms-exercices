"""
Linked List Module
"""


class Node:
    """
    Node Class
    """

    def __init__(self, value: int):
        self.value = value
        self.next: Node = None


class LinkedList:
    """
    Linked List Class
    """

    def __init__(self):
        self.first: Node = None

    def add_first(self, value: int) -> None:
        """
        Create node at begining of linked list
        """
        print(f"Adding {value}")
        node: Node = Node(value)
        node.next = self.first
        self.first = node

    def remove_first(self):
        """
        Remove first node from linked list
        """
        if self.first is not None:
            print(f"Removing {self.first.value}")
            self.first = self.first.next
        else:
            print("Empty list")

    def show(self):
        """
        Show all linked list
        """
        print("Show linked list: ", end = ' ')
        current: Node = self.first

        if not current:
            print('Empty list')
            return
        while current is not None:
            print(current.value, end = ' ')
            current = current.next
        print()

    def search(self, value):
        """
        Search and return value. If not found, return None
        """
        current: Node = self.first
        while current is not None:
            if current.value == value:
                print(f"Found value {value}! =)")
                return value
            current = current.next
        print(f"Value {value} not found! =(")
        return None

    def remove(self, value):
        """
        Remove node with value
        """

        current: Node = self.first

        if current is None:
            # Empty
            print(f"Cant remove {value}. Empty list")
            return

        # First element
        if current.value is value:
            print(f"Removing value {current.value}")
            self.first = current.next
            return

        # Middle elements
        while current.next is not None:
            if current.next.value == value:
                print(f"Removing value {current.next.value}")
                current.next = current.next.next
                return
            current = current.next

        # Last elemnt
        if current.value == value:
            print(f"Removing value {current.value}")
            current = None
            return

        # Not found
        print(f"Could not remove {value}. Value not found")


linked_list: LinkedList = LinkedList()
linked_list.show()

# Test add first
linked_list.add_first(1)
linked_list.show()
linked_list.add_first(2)
linked_list.show()
linked_list.add_first(3)
linked_list.show()

# Test search
linked_list.search(2)
linked_list.search(10)

# Test remove first
linked_list.remove_first()
linked_list.show()
linked_list.remove_first()
linked_list.show()
linked_list.remove_first()
linked_list.show()

# Test remove
linked_list.add_first(4)
linked_list.add_first(5)
linked_list.add_first(6)
linked_list.add_first(7)
linked_list.show()
linked_list.remove(20)
linked_list.remove(5)
linked_list.show()
linked_list.remove(6)
linked_list.show()
linked_list.remove(4)
linked_list.show()
linked_list.remove(7)
linked_list.show()
