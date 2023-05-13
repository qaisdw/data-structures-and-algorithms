class Node:
    def __init__(self,value,next_node=None):
        self.value = value
        self.next = next_node


class Linkedlist:
    def __init__(self,head=None):
        self.head = head

    def traverse(self):
        current_node = self.head
        while current_node:
            print(current_node.value)
            current_node = current_node.next

    def insert(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def includes(self, value):
        current_node = self.head
        while current_node:
            if current_node.value == value:
                print(current_node.value)
                return True
            current_node = current_node.next
        return False

    def to_string(self):
        values = ""
        current_node = self.head
        while current_node:
            values += "{ " + str(current_node.value) + " } -> "
            current_node = current_node.next
        values += "NULL"
        return values


