import heapq

class PriorityQueue:
    """Priority Queue using heapq (min-heap)."""
    def __init__(self):
        self._heap = []

    def enqueue(self, priority, item):
        heapq.heappush(self._heap, (priority, item))

    def dequeue(self):
        if not self._heap:
            raise IndexError("dequeue from empty priority queue")
        return heapq.heappop(self._heap)

    def display(self):
        print("PriorityQueue contents:", self._heap)


# ---------- TESTS ----------
if __name__ == "__main__":
    pq = PriorityQueue()
    pq.enqueue(2, "Task2")
    pq.enqueue(1, "Task1")
    pq.enqueue(3, "Task3")
    pq.display()
    assert pq.dequeue() == (1, "Task1")
    pq.display()
    assert pq.dequeue() == (2, "Task2")
    print("✅ All PriorityQueue test cases passed successfully!")
