from collections import deque

class Queue:
    """Queue implementation (FIFO) using deque."""
    def __init__(self):
        self._dq = deque()

    def enqueue(self, item):
        self._dq.append(item)

    def dequeue(self):
        if not self._dq:
            raise IndexError("dequeue from empty queue")
        return self._dq.popleft()

    def peek(self):
        if not self._dq:
            raise IndexError("peek from empty queue")
        return self._dq[0]

    def size(self):
        return len(self._dq)

    def display(self):
        print("Queue contents:", list(self._dq))


# ---------- TESTS ----------
if __name__ == "__main__":
    q = Queue()
    q.display()
    q.enqueue("A"); q.enqueue("B"); q.enqueue("C")
    q.display()
    assert q.peek() == "A"
    removed = q.dequeue(); print("Dequeued:", removed)
    assert removed == "A"
    q.display()
    assert q.size() == 2
    print("✅ All Queue test cases passed successfully!")
