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
        while current is not None:
            print(current.value, end = ' ')
            current = current.next
        print()


linked_list: LinkedList = LinkedList()
linked_list.show()

linked_list.add_first(1)
linked_list.show()

linked_list.add_first(2)
linked_list.show()

linked_list.add_first(3)
linked_list.show()

linked_list.remove_first()
linked_list.show()

linked_list.remove_first()
linked_list.show()

linked_list.remove_first()
linked_list.show()
