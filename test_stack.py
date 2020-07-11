import pytest

from stack import Stack


def test_processes_elements_in_lifo_order():
    stack = Stack()

    stack.push(5)
    stack.push(0)
    stack.push("Test")

    assert stack.pop() == "Test"
    assert stack.pop() == 0
    assert stack.pop() == 5


def test_peek_returns_correct_element():
    stack = Stack()

    stack.push(1)
    stack.push(37)

    assert stack.peek() == 37


def test_peek_does_not_remove_element():
    stack = Stack()
    for i in range(5):
        stack.push(i)

    stack.peek()
    assert len(stack) == 5


def test_popping_empty_stack_raises_exception():
    stack = Stack()

    with pytest.raises(RuntimeError) as ctx:
        stack.pop()
