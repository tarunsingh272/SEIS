# from realpython.com...

# python -m pytest -v --cov

# Since conda don't know about pythonds3, instead run command:
#
# pip install pythonds3
from stack import Stack

import pytest

@pytest.fixture
def stack():
    return Stack()

def test_constructor():
    s = Stack()
    assert isinstance(s, Stack)
    assert len(s) == 0

def test_push(stack): # uses a fixture to start with an empty Stack
    stack.push(3)
    assert len(stack) == 1
    stack.push(5)
    assert len(stack) == 2

def test_pop(stack): # uses a fixture to start with an empty Stack
    stack.push("hello")
    stack.push("world")
    assert stack.pop() == "world"
    assert stack.pop() == "hello"
    assert stack.pop() is None
