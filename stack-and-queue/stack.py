class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

class Stack:
    def __init__(self):
        self.top = None  # top node of the stack

    def push(self, value):
        node = Node(value)
        if self.is_empty():
            self.top = node
        else:
            node.next_node = self.top
            self.top = node

    def pop(self):
        if self.is_empty():
            raise ValueError("Stack is empty. There is nothing to pop from the stack.")

        value = self.top.value
        self.top = self.top.next_node
        return value

    def peek(self):
        if self.is_empty():
            raise ValueError("Stack is empty. There is nothing to peek to in the queue.")

        return self.top.value

    def is_empty(self):
        return self.top is None
    
    def __str__(self):
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
    s.pop()
    print(s.is_empty())
    print(s)
