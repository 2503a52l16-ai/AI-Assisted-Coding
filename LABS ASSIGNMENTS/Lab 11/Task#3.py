class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """Singly Linked List with insert and display."""
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = new_node

    def display(self):
        cur = self.head
        vals = []
        while cur:
            vals.append(cur.data)
            cur = cur.next
        print("LinkedList contents:", vals)
        return vals


# ---------- TESTS ----------
if __name__ == "__main__":
    ll = LinkedList()
    ll.insert(10); ll.insert(20); ll.insert(30)
    vals = ll.display()
    assert vals == [10, 20, 30]
    ll.insert(40)
    assert ll.display() == [10, 20, 30, 40]
    print("✅ All LinkedList test cases passed successfully!")
