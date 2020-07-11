from dataclasses import dataclass
from typing import Optional, Any


@dataclass
class ListNode:
    value: Any
    next: Optional["ListNode"]


class LinkedList:

    def __init__(self):
        self._first = ListNode(None, None)
        self._last = self._first

    def append(self, item):
        new_node = ListNode(item, None)
        self._last.next = new_node
        self._last = new_node

    def __iter__(self):
        current_node = self._first

        while current_node is not self._last:
            current_node = current_node.next
            yield current_node.value

    def insert(self, pos, item):
        current_node = self._first

        try:
            for _ in range(pos):
                current_node = current_node.next

            new_node = ListNode(value=item, next=current_node.next)
            current_node.next = new_node
        except TypeError:
            raise ValueError(f"List too short, cannot insert at {pos}")

    def __getitem__(self, item):
        print(f"Get item {item}")
        return 42

    def __setitem__(self, key, value):
        print(f"Set item {key} {value}")

    def __delitem__(self, key):
        pass


if __name__ == '__main__':
    my_list = LinkedList()
    my_list.append(1)
    my_list.append("Kot")
    my_list.append({"foo": "bar"})
    my_list.insert(0, 10)
    my_list.insert(1, 5)

    for item in my_list:
        print(item)
