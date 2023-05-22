class Node:
    def __init__(self, value, next_node=None):
        """
        Initialize a Node object.

        Args:
            value: The value of the node.
            next_node: Reference to the next node in the linked list (default is None).
        """
        self.value = value
        self.next_node = next_node


class Linkedlist:
    def __init__(self, head=None):
        """
        Initialize a Linkedlist object.

        Args:
            head: The head node of the linked list (default is None).
        """
        self.head = head

    def traverse(self):
        """
        Traverse the linked list and print the values of all nodes.
        """
        current_node = self.head
        while current_node:
            print(current_node.value)
            current_node = current_node.next_node

    def insert(self, value):
        """
        Insert a new node with the given value at the beginning of the linked list.

        Args:
            value: The value of the node to be inserted.
        """
        new_node = Node(value)
        new_node.next_node = self.head
        self.head = new_node

    def includes(self, value):
        """
        Check if a node with the given value exists in the linked list.

        Args:
            value: The value to search for.

        Returns:
            True if the value is found, False otherwise.
        """
        current_node = self.head
        while current_node:
            if current_node.value == value:
                print(current_node.value)
                return True
            current_node = current_node.next_node
        return False

    def to_string(self):
        """
        Convert the linked list to a string representation.

        Returns:
            String representation of the linked list.
        """
        values = "head -> "
        current_node = self.head
        while current_node:
            values += "{ " + str(current_node.value) + " } -> "
            current_node = current_node.next_node
        values += "NULL"
        return values

    def append(self, value):
        """
        Append a new node with the given value to the end of the linked list.

        Args:
            value: The value of the node to be appended.
        """
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next_node:
                current_node = current_node.next_node
            current_node.next_node = new_node

    def addBefore(self, value, target_node):
        """
        Insert a new node with the given value before the first occurrence of the target node.

        Args:
            value: The value of the node to be inserted.
            target_node: The value of the target node.
        """
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
        """
        Insert a new node with the given value after the first occurrence of the target node.

        Args:
            value: The value of the node to be inserted.
            target_node: The value of the target node.
        """
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
        """
        Delete the first occurrence of a node with the given value from the linked list.

        Args:
            value: The value of the node to be deleted.
        """
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
        """
        Calculate the length of the linked list.

        Returns:
            The length of the linked list.
        """
        length = 0
        current_node = self.head
        while current_node:
            length += 1
            current_node = current_node.next_node
        return length
    
    def kthFromEnd(self, k):
        """
        Find the value of the k-th node from the end of the linked list.

        Args:
            k: The index of the node from the end (starting from 0).

        Returns:
            The value of the k-th node from the end.
        """
        length = self.linkLength()

        if self.head is None:
            print("Linked list is empty!")
            return

        if k < 0:
            raise IndexError("Enter positive index only")

        if k >= length:
            raise IndexError("Index out of range")

        current_node = self.head
        for _ in range(length - k - 1):
            current_node = current_node.next_node
        return current_node.value
    
    def kthFormEndIndex(self, k):
        """
        Find the index of the first occurrence of a node with the given value in the linked list.

        Args:
            k: The value to search for.

        Returns:
            The index of the first occurrence of the node, or -1 if not found.
        """
        current_node = self.head
        index = 0
        while current_node:
            if current_node.value == k:
                return index
            current_node = current_node.next_node
            index += 1
        return -1
    
    @staticmethod
    def zip_LL(list1, list2):
        """
        Merge two linked lists by alternating their nodes.

        Args:
            list1: The head node of the first linked list.
            list2: The head node of the second linked list.

        Returns:
            A new instance of the  linked list representing the merged result.
        """
        if not list1 and not list2:
            raise Exception("You cannot merge empty lists")
        
        head = list1
        current1 = list1
        current2 = list2

        while current1.next_node and current2:
            next1 = current1.next_node
            next2 = current2.next_node

            current1.next_node = current2
            current2.next_node = next1

            current1 = next1
            current2 = next2

        if current2:
            current1.next_node = current2

        return Linkedlist(head)






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

    n = Node(1)
    app1 = Linkedlist(n)
    app1.append(3)
    app1.append(2)

    n2 = Node(5)
    app2 = Linkedlist(n2)
    app2.append(9)
    app2.append(7)
    app2.append(8)
    app2.append(9)
    app2.append(10)

    zipll = Linkedlist.zip_LL(app1.head, app2.head)

    current_node = zipll.head
    while current_node:
        print(current_node.value)
        current_node = current_node.next_node

    print(zipll.to_string())

