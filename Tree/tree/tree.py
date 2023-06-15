class Node :
    def __init__(self,value=None,next=None):
        self.value = value
        self.next = next
    
class Queue:
    def __init__(self,front=None,back=None):
        self.front = front # first node in th queue
        self.back=back    # last node in queue    

    def  enqueue(self,value) :
        '''
        adds a new node with that value to the back of the queue with an O(1) Time performance

        '''
        node = Node(value)
        if self.front is None:
            self.back = node
            self.front = node
        else:
            self.back.next= node
            self.back = node 



    def dequeue(self):
        '''
        Removes the node from the front of the queue and
        Returns the value from node from the front of the queue

        '''
        if self.front is None:
            raise IndexError("The queue is empty!!")
        else:
            temp = self.front
            self.front = temp.next
            temp.next = None
            return temp.value
        

    def peek(self):
        '''
        Returns Value of the node located at front of the queue

        '''
        if self.front == None:
            raise IndexError("The queue is empty!!")
        else:
            return self.front.value
        

    def is_empty(self):
        '''
        this method return Boolean indicating whether or not the queue is empty.
        
        '''
        if self.front == None:
            return True
        else:
            return False
    
    
    def __str__(self):
        current=self.front
        string=""
        while current:
            string+=f"{current.value}"
            string+=" -> "
            current=current.next
        return string+"None"



class Tnode:
  def __init__(self,value):
    self.value=value
    self.right= None
    self.left = None
   

class Tree:
  def __init__(self):
    self.root=None

  def breadth_first(self):
    '''
    Breadth first traversal iterates through the tree by going through each level of the tree node-by-node. 
    '''
    if not self.root:
      return self.root
      
    output = []
    queue = Queue()
    queue.enqueue(self.root)

    while not queue.is_empty():
      
      front = queue.dequeue()
      output.append(front.value)
      
      if front.left :
          queue.enqueue(front.left)
          
      if front.right :
          queue.enqueue(front.right) 
          
        
    return output

  def pre_order(self):
    '''
    going through the depth (height) of the tree first
    root >>>>> left >>>> right
    '''
    if self.root == None :
       return None
    list_ = []
    def _walk(root):
      #root
      list_.append(root.value)

      #left
      if root.left :
        _walk(root.left)
        
      #right
      if root.right :
        _walk(root.right)

    _walk(self.root)
    return list_

  def in_order(self):
    '''
    going through the depth (height) of the tree first
    left >>>> root >>>> right
    '''
    list_ = []  
    def _walk(root):
      #left
      if root.left :
        _walk(root.left)
        
      #root
      list_.append(root.value)

      #right
      if root.right :
        _walk(root.right)

    _walk(self.root)
    return list_
  

  def post_order(self):
    '''
    going through the depth (height) of the tree first
    left >>>> right >>>> root
    '''
    list_ = []  
    def _walk(root):
      #left
      if root.left :
        _walk(root.left)
        
      #right
      if root.right :
        _walk(root.right)

      #root
      list_.append(root.value)

    _walk(self.root)
    return list_
  

 
    



class binary_search_tree(Tree):


  def Add(self,value):
    '''
    Adds a new node with that value in the correct location in the binary search tree.
    '''
    
    if self.root == None:
      self.root == Tnode(value) 
      return
    
    current = self.root
    while current : 
      if value < current.value: 
        if current.left == None:
          current.left = Tnode(value)
          return
        else:
          current = current.left
          continue

      if value > current.value :
        if current.right == None:
          current.right = Tnode(value)
          return
        else:
          current = current.right
          continue


  
  def Contains(self,value):
    '''
    Returns boolean indicating whether or not the value is in the tree at least once.
    '''
    current = self.root
    if value == current.value: 
      return True
    
    while current : 
      if value < current.value: 
        if current.left == None:
          return False
        elif value == current.left.value :
          return True
        else:
          current = current.left
          continue

      if value > current.value :
        if current.right == None:
          return False
        elif value == current.right.value:
          return True
        else:
          current = current.right
          continue
    return False
  



  
    
   

    
     

     

          
      
         

      
    
    


 