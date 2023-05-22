# from realpython.com...

# python -m pytest -v --cov

# Since conda don't know about pythonds3, instead run command:
#
# pip install pythonds3
# from pythonds3 import Stack
# from ds.stack import Stack
import pytest
from stack import Stack
@pytest.fixture
def stack():
    return Stack()

def test_constructor():
    s = Stack()
    assert isinstance(s, Stack)
    assert s.is_empty()

def test_push(stack):
    stack.push(3)
    assert stack.size() == 1
    stack.push(5)
    assert stack.size() == 2

def test_pop(stack):
    stack.push("hello")
    stack.push("world")
    assert stack.pop() == "world"
    assert stack.pop() == "hello"
    # assert stack.pop() is None
