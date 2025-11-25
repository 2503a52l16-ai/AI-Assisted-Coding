class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.map = {}
        self.head = Node(None, None)
        self.tail = Node(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _add_front(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def _move_front(self, node):
        self._remove(node)
        self._add_front(node)

    def get(self, key):
        if key not in self.map:
            return None
        node = self.map[key]
        self._move_front(node)
        return node.value

    def put(self, key, value):
        if key in self.map:
            node = self.map[key]
            node.value = value
            self._move_front(node)
            return

        if len(self.map) == self.capacity:
            lru = self.tail.prev
            self._remove(lru)
            del self.map[lru.key]

        new_node = Node(key, value)
        self.map[key] = new_node
        self._add_front(new_node)

    def __repr__(self):
        cur = self.head.next
        out = []
        while cur != self.tail:
            out.append(f"{cur.key}:{cur.value}")
            cur = cur.next
        return " -> ".join(out)

def demo_lru():
    cache = LRUCache(2)
    cache.put("P1", "Product 1")
    cache.put("P2", "Product 2")
    print("Cache:", cache)

    cache.get("P1")
    print("After get(P1):", cache)

    cache.put("P3", "Product 3")  # should evict P2
    print("After put(P3):", cache)

# Execution
demo_lru()
