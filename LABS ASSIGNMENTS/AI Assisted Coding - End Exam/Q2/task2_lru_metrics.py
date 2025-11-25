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

        self.hits = 0
        self.misses = 0
        self.evictions = 0

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
            self.misses += 1
            return None
        node = self.map[key]
        self._move_front(node)
        self.hits += 1
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
            self.evictions += 1

        new_node = Node(key, value)
        self.map[key] = new_node
        self._add_front(new_node)

    def stats(self):
        return {
            "hits": self.hits,
            "misses": self.misses,
            "evictions": self.evictions
        }

    def __repr__(self):
        cur = self.head.next
        result = []
        while cur != self.tail:
            result.append(f"{cur.key}:{cur.value}")
            cur = cur.next
        return " -> ".join(result)

def demo_lru_metrics():
    cache = LRUCache(2)

    cache.put("P1", "Product 1")
    cache.put("P2", "Product 2")

    cache.get("P1")  # hit
    cache.put("P3", "Product 3")  # evict P2
    cache.get("P2")  # miss
    cache.get("P3")  # hit

    print("Final Cache:", cache)
    print("Metrics:", cache.stats())

# Execution
demo_lru_metrics()
