class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node


class Linkedlist:
    def __init__(self, head=None):
        self.head = head

    def traverse(self):
        current_node = self.head
        while current_node:
            print(current_node.value)
            current_node = current_node.next_node

    def insert(self, value):
        new_node = Node(value)
        new_node.next_node = self.head
        self.head = new_node

    def includes(self, value):
        current_node = self.head
        while current_node:
            if current_node.value == value:
                print(current_node.value)
                return True
            current_node = current_node.next_node
        return False

    def to_string(self):
        values = "head -> "
        current_node = self.head
        while current_node:
            values += "{ " + str(current_node.value) + " } -> "
            current_node = current_node.next_node
        values += "NULL"
        return values

    def append(self, value):
        newNode = Node(value)

        if self.head is None:
            self.head = newNode
        else:
            current_node = self.head
            while current_node.next_node:
                current_node = current_node.next_node
            current_node.next_node = newNode

    def addBefore(self, value, target_node):
        newNode = Node(value)

        if self.head is None:
            print("Linked list is empty!")
            return

        if self.head.value == target_node:
            newNode.next_node = self.head
            self.head = newNode
            return

        current_node = self.head
        while current_node.next_node:
            if current_node.next_node.value == target_node:
                break
            current_node = current_node.next_node

        if current_node.next_node is None:
            print("Node is not found")
        else:
            newNode.next_node = current_node.next_node
            current_node.next_node = newNode

    def addAfter(self, value, target_node):
        newNode = Node(value)

        if self.head is None:
            print("Linked list is empty!")
            return

        current_node = self.head
        while current_node:
            if current_node.value == target_node:
                break
            current_node = current_node.next_node

        if current_node is None:
            print("Node is not found")
        else:
            newNode.next_node = current_node.next_node
            current_node.next_node = newNode

    def delete(self, value):
        if self.head is None:
            print("Linked list is empty!")
            return

        if self.head.value == value:
            self.head = self.head.next_node
            return

        current_node = self.head
        prev_node = None

        while current_node:
            if current_node.value == value:
                break
            prev_node = current_node
            current_node = current_node.next_node

        if current_node is None:
            print("Node is not found")
            return
        prev_node.next_node = current_node.next_node

    def linkLength(self):
        length = 0
        current_node = self.head
        while current_node:
            length += 1
            current_node = current_node.next_node
        return length
    
    def kthFromEnd(self, k):
        length = self.linkLength()

        if self.head is None:
            print("Linked list is empty!")
            return

        if k < 0:
            raise IndexError ("Enter positive index only")

        if k > length:
            raise IndexError ("index out of the range")

        current_node = self.head
        for _ in range(length - k - 1):
            current_node = current_node.next_node
        return current_node.value
    
    def kthFormEndIndex(self, k):
        current_node = self.head
        index = 0
        while current_node:
            if current_node.value == k:
                return index
            current_node = current_node.next_node
            index += 1
        return -1




        
        






if __name__ == "__main__":
    head = Node(1)
    head.next_node = Node(3)
    head.next_node.next_node = Node(2)
    app = Linkedlist(head)

    app.append(5)

    app.addBefore(3, 5)

    app.addAfter(3, 5)
    app.delete(5)


    current_node = app.head
    while current_node:
        print(current_node.value)
        current_node = current_node.next_node

    print("last node",app.kthFromEnd(4))
    print(app.linkLength())
    print("middle node", app.kthFormEndIndex(1))

    print()
    print("Initial List:")
    print(app.to_string())
