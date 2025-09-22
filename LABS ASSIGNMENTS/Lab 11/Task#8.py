from collections import deque

class DequeDS:
    """Double-ended queue using collections.deque."""
    def __init__(self):
        self._dq = deque()

    def append_left(self, item):
        self._dq.appendleft(item)

    def append_right(self, item):
        self._dq.append(item)

    def pop_left(self):
        return self._dq.popleft()

    def pop_right(self):
        return self._dq.pop()

    def display(self):
        print("Deque contents:", list(self._dq))


# ---------- TESTS ----------
if __name__ == "__main__":
    dq = DequeDS()
    dq.append_right(10); dq.append_left(5); dq.append_right(15)
    dq.display()
    assert dq.pop_left() == 5
    dq.display()
    assert dq.pop_right() == 15
    print("✅ All Deque test cases passed successfully!")
