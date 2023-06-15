class Node:
    def __init__(self, value=None, next_node=None):
        """
        Initialize a Node object.

        Args:
            value: The value to be stored in the node.
            next_node: The reference to the next node in the linked list.
        """
        self.value = value
        self.next_node = next_node

class Queue:
    def __init__(self):
        """
        Initialize an empty Queue object.
        """
        self.front = None  # first node in the queue
        self.back = None   # last node in the queue

    def enqueue(self, value):
        """
        Adds a value to the back of the queue.

        Args:
            value: The value to be added to the queue.
        """
        node = Node(value)
        if self.is_empty():
            self.front = node
        else:
            self.back.next_node = node
        self.back = node

    def dequeue(self):
        """
        Removes and returns the value from the front of the queue.

        Returns:
            The value that was removed from the queue.

        Raises:
            ValueError: If the queue is empty.
        """
        if self.is_empty():
            raise ValueError("Queue is empty. There is nothing to remove from the queue")

        temp = self.front
        self.front = temp.next_node
        temp.next_node = None

        return temp.value

    def peek(self):
        """
        Returns the value from the front of the queue without removing it.

        Returns:
            The value from the front of the queue.

        Raises:
            ValueError: If the queue is empty.
        """
        if self.is_empty():
            raise ValueError("Queue is empty. There is nothing to peek in the queue")

        return self.front.value

    def is_empty(self):
        """
        Checks if the queue is empty.

        Returns:
            True if the queue is empty, False otherwise.
        """
        return self.front is None
    
    def __str__(self):
        """
        Returns a string representation of the queue.

        Returns:
            A string representation of the queue.
        """
        values = "head -> "
        current_node = self.front
        while current_node:
            values += "{ " + str(current_node.value) + " } -> "
            current_node = current_node.next_node
        values += "NULL"
        return values

if __name__ == "__main__":
    q = Queue()
    q.enqueue("first")
    q.enqueue("sec")
    q.enqueue("ther")
    q.enqueue("forth")
    print(q)
    print(q.peek())
    q.dequeue()
    q.dequeue()
    q.dequeue()
    print("deleted value = " ,q.dequeue())
    print(q)
