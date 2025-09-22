from collections import deque
from typing import List, Dict, Optional

class CafeteriaOrderQueue:
    """
    Cafeteria Order Queue using FIFO (First-In-First-Out) principle.
    Stores student orders and serves them in order of arrival.
    """

    def __init__(self):
        self._queue: deque[Dict[str, List[str]]] = deque()

    def enqueue(self, student_id: int, items: List[str]) -> None:
        """Add a student's order to the queue."""
        order = {"student_id": student_id, "items": items}
        self._queue.append(order)
        print(f"✅ Order added: {order}")

    def dequeue(self) -> Optional[Dict[str, List[str]]]:
        """Serve the next order in the queue. Returns None if queue is empty."""
        if not self._queue:
            print("⚠️ No orders to serve.")
            return None
        order = self._queue.popleft()
        print(f"🍽 Served: {order}")
        return order

    def peek(self) -> Optional[Dict[str, List[str]]]:
        """Return the next order without removing it, or None if queue is empty."""
        return self._queue[0] if self._queue else None

    def size(self) -> int:
        """Return the number of orders in the queue."""
        return len(self._queue)

    def display(self) -> None:
        """Display all pending orders in the queue."""
        if not self._queue:
            print("The queue is empty.")
        else:
            print("📋 Pending Orders:")
            for i, order in enumerate(self._queue, start=1):
                print(f"{i}. Student {order['student_id']} → Items: {order['items']}")

    def __str__(self) -> str:
        """Return a string representation of the queue."""
        return "\n".join(f"Student {o['student_id']} → {o['items']}" for o in self._queue)


# ---------- TESTS ----------
if __name__ == "__main__":
    cq = CafeteriaOrderQueue()
    cq.enqueue(101, ["Sandwich", "Juice"])
    cq.enqueue(102, ["Burger"])
    cq.enqueue(103, ["Pizza", "Soda"])
    print()
    cq.display()
    assert cq.size() == 3

    first_order = cq.dequeue()
    assert first_order["student_id"] == 101
    print()
    cq.display()

    next_order = cq.peek()
    assert next_order["student_id"] == 102

    print("\n✅ All Cafeteria Queue test cases passed successfully!")
