class Node :
    def __init__(self,value=None,next=None):
        self.value = value
        self.next = next

class Stack:
    def __init__(self,top=None):
        self.top = top

        

    def push(self,value):
        '''
        This method adds a new node with that value 
        to the top of the stack with an O(1) Time performance.
 
        '''
        node = Node(value)

        if self.top == None :
            self.top = node
        else:
            node.next = self.top
            self.top = node



    def pop(self):
        '''
        This method returns the value from node from
        the top of the stack and Removes the node from the
        top of the stack

        '''
        if self.top is None:
            raise IndexError("The stack is empty!!")
        else:
            temp= self.top
            self.top = temp.next
            temp.next = None
            return temp.value

    


    def peek(self):
        '''
        Returns Value of the node located at the top of the stack

        '''
        if self.top == None:
            raise IndexError("The stack is empty!!")
        else:
            return self.top.value
        

    def is_empty(self):
        '''
        this method return Boolean indicating whether or not the stack is empty.
        
        '''
        if self.top == None:
            return True
        else:
            return False

    def __str__(self):
        current=self.top
        string=""
        while current:
            string+=f"{current.value}"
            string+=" -> "
            current=current.next
        return string+"None"  

 
 
class PseudoQueue:

    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def enqueue(self, value):
        '''
        Inserts a value into the PseudoQueue, using a first-in, first-out approach.
        '''
        self.stack1.push(value)

    def dequeue(self):
        '''
        Extracts a value from the PseudoQueue, using a first-in, first-out approach.
        '''
        if self.stack1.is_empty() and self.stack2.is_empty():
            raise IndexError("The queue is empty!!")
        while not self.stack1.is_empty():
            self.stack2.push(self.stack1.pop())
        self.stack2.pop()
        while not self.stack2.is_empty():
            self.stack1.push(self.stack2.pop())
        return self.stack1


    