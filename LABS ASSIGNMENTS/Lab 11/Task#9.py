def display_comparison():
    table = """\
| Data Structure | Insert | Search | Delete | Remarks |
|----------------|--------|--------|--------|---------|
| Stack | O(1) | O(n) | O(1) | LIFO operations |
| Queue | O(1) | O(n) | O(1) | FIFO operations |
| Linked List | O(1) at head | O(n) | O(1) with node | Sequential access only |
| BST (balanced) | O(log n) | O(log n) | O(log n) | Sorted storage |
| Hash Table | O(1) avg | O(1) avg | O(1) avg | Depends on hash function |
| Graph (adj list) | O(1) | O(V+E) | O(E) | Good for networks |
| Priority Queue | O(log n) | O(n) | O(log n) | Uses heap |
| Deque | O(1) | O(n) | O(1) | Double-ended flexibility |
"""
    print(table)


# ---------- TESTS ----------
if __name__ == "__main__":
    display_comparison()
    print("✅ Data Structure comparison table displayed successfully!")
