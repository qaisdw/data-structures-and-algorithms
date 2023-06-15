import pytest
from queuee import Queue



def test_queue_enqueue():
    queue = Queue()
    queue.enqueue(10)
    assert queue.peek() == 10

def test_queue_enqueue_multiple():
    queue = Queue()
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    assert queue.peek() == 10

def test_queue_dequeue():
    queue = Queue()
    queue.enqueue(10)
    queue.enqueue(20)
    assert queue.dequeue() == 10

def test_queue_empty_after_dequeues():
    queue = Queue()
    queue.enqueue(10)
    queue.enqueue(20)
    queue.dequeue()
    queue.dequeue()
    assert queue.is_empty()

def test_queue_peek():
    queue = Queue()
    queue.enqueue(10)
    queue.enqueue(20)
    assert queue.peek() == 10

def test_queue_instantiate_empty():
    queue = Queue()
    assert queue.is_empty()

def test_queue_dequeue_and_peek_on_empty():
    queue = Queue()
    with pytest.raises(ValueError):
        queue.dequeue()