import pytest
from stack import Stack


 
def test_stack_push():
    stack = Stack()
    stack.push(10)
    assert stack.peek() == 10

def test_stack_push_multiple():
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    assert stack.peek() == 30

def test_stack_pop():
    stack = Stack()
    stack.push(10)
    stack.push(20)
    assert stack.pop() == 20

def test_stack_empty_after_pops():
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.pop()
    stack.pop()
    assert stack.is_empty()

def test_stack_peek():
    stack = Stack()
    stack.push(10)
    stack.push(20)
    assert stack.peek() == 20

def test_stack_instantiate_empty():
    stack = Stack()
    assert stack.is_empty()

def test_stack_pop_on_empty():
    stack = Stack()
    with pytest.raises(ValueError):
        stack.pop() == "Queue is empty. There is nothing to remove from the queue"

def test_stack_peek_on_empty():
    stack = Stack()
    with pytest.raises(ValueError):
        stack.peek() == "Stack is empty. There is nothing to peek to in the queue."
