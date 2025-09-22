class HashTable:
    """Hash Table with chaining for collision handling."""
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        idx = self._hash(key)
        for i, (k, v) in enumerate(self.table[idx]):
            if k == key:
                self.table[idx][i] = (key, value)
                return
        self.table[idx].append((key, value))

    def search(self, key):
        idx = self._hash(key)
        for k, v in self.table[idx]:
            if k == key:
                return v
        return None

    def delete(self, key):
        idx = self._hash(key)
        for i, (k, v) in enumerate(self.table[idx]):
            if k == key:
                del self.table[idx][i]
                return True
        return False

    def display(self):
        print("HashTable contents:", self.table)


# ---------- TESTS ----------
if __name__ == "__main__":
    ht = HashTable()
    ht.insert("name", "Alice")
    ht.insert("age", 25)
    ht.display()
    assert ht.search("name") == "Alice"
    assert ht.delete("age") == True
    ht.display()
    assert ht.search("age") is None
    print("✅ All HashTable test cases passed successfully!")
