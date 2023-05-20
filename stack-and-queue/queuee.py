class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

class Queue:
    def __init__(self):
        self.front = None  # first node in the queue
        self.back = None   # last node in the queue

    def enqueue(self, value):
        node = Node(value)
        if self.is_empty():
            self.front = node
        else:
            self.back.next_node = node
        self.back = node

    def dequeue(self):
        if self.is_empty():
            raise ValueError("Queue is empty. There is nothing to remove from the queue")

        temp = self.front
        self.front = temp.next_node
        if self.front is None:
            self.back = None

        return temp.value

    def peek(self):
        if self.is_empty():
            raise ValueError("Queue is empty. There is nothing to peek in the queue")

        return self.front.value

    def is_empty(self):
        return self.front is None
    
    def __str__(self):
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
    q.dequeue()
    print(q)
