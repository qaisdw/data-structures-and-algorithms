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

class Stack:
    def __init__(self):
        """
        Initialize an empty Stack object.
        """
        self.top = None  # top node of the stack

    def push(self, value):
        """
        Pushes a value onto the top of the stack.

        Args:
            value: The value to be pushed onto the stack.
        """
        node = Node(value)
        if self.is_empty():
            self.top = node
        else:
            node.next_node = self.top
        self.top = node

    def pop(self):
        """
        Removes and returns the value from the top of the stack.

        Returns:
            The value that was popped from the stack.

        Raises:
            ValueError: If the stack is empty.
        """
        if self.is_empty():
            raise ValueError("Stack is empty. There is nothing to pop from the stack.")

        temp = self.top
        self.top = temp.next_node
        temp.next_node = None

        return temp.value

    def peek(self):
        """
        Returns the value from the top of the stack without removing it.

        Returns:
            The value from the top of the stack.

        Raises:
            ValueError: If the stack is empty.
        """
        if self.is_empty():
            raise ValueError("Stack is empty. There is nothing to peek to in the queue.")

        return self.top.value

    def is_empty(self):
        """
        Checks if the stack is empty.

        Returns:
            True if the stack is empty, False otherwise.
        """
        return self.top is None
    
    def __str__(self):
        """
        Returns a string representation of the stack.

        Returns:
            A string representation of the stack.
        """
        values = "head -> "
        current_node = self.top
        while current_node:
            values += "{ " + str(current_node.value) + " } -> "
            current_node = current_node.next_node
        values += "NULL"
        return values

if __name__ == "__main__":
    s = Stack()
    s.push("first")
    s.push("sec")
    s.push("ther")
    s.push("forth")
    print(s.peek())
    print(s)
    s.pop()
    s.pop()
    print(s)
    print(s.is_empty())
    s.pop()
    print("deleted value =",s.pop())
    print(s.is_empty())
    print(s)
