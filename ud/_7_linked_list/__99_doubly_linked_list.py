"""
Doubly Linked List Module
"""


class Node:
    """
    Node class
    """

    def __init__(self, value: int):
        self.value = value
        self.next = None
        self.prev = None

    def show(self):
        """
        Print node value
        """
        print(f"Node {self.value}")


class DoublyLinkedList:
    """
    Doubly Linked List Class
    """

    def __init__(self):
        self.first = None
        self.last = None

    def __is_empty(self):
        return self.first is None

    def insert_first(self, value: int):
        """
        Insert value at first position
        """

        # Create node
        node: Node = Node(value=value)

        # Case first (empty list)
        if self.first is None:
            self.first = self.last = node

        # Case not first
        else:
            node.next = self.first
            self.first.prev = node
            node.prev = None
            self.first = node

    def insert_last(self, value: int):
        """
        Insert value at last position
        """

         # Create node
        node: Node = Node(value=value)

        # Case first (empty list)
        if self.first is None:
            self.first = self.last = node

        # Case not first
        else:
            node.next = None
            self.last.next = node
            node.prev = self.last
            self.last = node

    def remove_first(self):
        """
        Remove value from first position
        """

        if self.first is None:
            print("Empty list")
        else:
            print(f"Removing first ({self.first.value}) ... ")
            self.first.prev = None
            self.first = self.first.next

    def remove_last(self):
        """
        Remove value from last position
        """

        if self.first is None:
            print("Empty list")
        else:
            print(f"Removing last ({self.last.value}) ... ")
            self.last.prev.next = None
            self.last = self.last.prev

    def show_asc(self):
        """
        Show linked lisk from left to right
        """

        print("Show asc [first, ..., last]: ", end=' ')
        if self.__is_empty():
            print("List empty")
        else:
            temp = self.first
            while temp is not None:
                print(temp.value, end=' ')
                temp = temp.next
        print()

    def show_desc(self):
        """
        Show linked lisk from right to left
        """

        print("Show desc [last, ..., first]: ", end=' ')
        if self.__is_empty():
            print("List empty")
        else:
            temp = self.last
            while temp is not None:
                print(temp.value, end=' ')
                temp = temp.prev
        print()

    def remove_value(self, value:int):
        """
        Search value, and remove it
        """

        if self.__is_empty():
            print("Cant remove. Empty list")
        else:

            # If first:
            if self.first.value == value:
                self.remove_first()
                return

            # If last:
            if self.last.value == value:
                self.remove_last()
                return

            # If middle, search it:
            temp = self.first
            while temp.value != value:
                temp = temp.next
                if temp is None:
                    print("Cant remove. Value is not found")
                    return

            # Remove
            temp.prev.next = temp.next
            temp.next.prev = temp.prev

my_list: DoublyLinkedList = DoublyLinkedList()
my_list.show_asc()
my_list.insert_first(1)
my_list.insert_first(2)
my_list.show_asc()

my_list.insert_last(0)
my_list.insert_last(-1)
my_list.show_asc()

my_list.insert_first(3)
my_list.insert_last(-2)
my_list.insert_last(-3)
my_list.show_asc()

my_list.show_desc()

my_list.remove_first()
my_list.show_asc()

my_list.remove_last()
my_list.show_asc()

my_list.remove_value(0)
my_list.show_asc()

my_list.remove_value(-2)
my_list.show_asc()

my_list.remove_value(2)
my_list.show_asc()