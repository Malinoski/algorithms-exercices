"""
Priority class module
"""


class PriorityQueue:
    """
    Priority Queue class
    """

    def __init__(self, capacity):
        self.capacity = capacity
        self.values = [None for _ in range(capacity)]
        self.quantity_values = 0

    def is_full(self) -> bool:
        """
        Check if queue is full
        """
        return self.capacity == self.quantity_values

    def is_empty(self) -> bool:
        """
        Check if queue is empty
        """
        return self.quantity_values == 0

    def queue(self, value):
        """
        Insert value at queue, following priority, where less number has priority from higher
        """

        # check if full
        if self.is_full():
            print("Queue is full")
        else:
            # Queue is not full
            if self.quantity_values == 0:
                self.values[0] = value
                print(f"Inserted {value} at first position! {self.values}")
            else:
                i = self.quantity_values - 1

                # Shift elements to right
                while i >= 0:
                    if value > self.values[i]:
                        self.values[i+1] = self.values[i]
                        self.values[i] = None
                        print(f"Shifted {self.values[i+1]} to rigth ... {self.values}")
                        i -= 1
                    else:
                        break
                i += 1

                # Insert value
                self.values[i] = value
                print(f"Inserted {value} at position {i}. {self.values}")
            self.quantity_values += 1

queue = PriorityQueue(7)
queue.queue(1)
queue.queue(3)
queue.queue(2)
queue.queue(2)
queue.queue(9)
queue.queue(0)
