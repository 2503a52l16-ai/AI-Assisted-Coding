# -----------------------------
# Task 4: Inventory Class
# -----------------------------

class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, name, quantity):
        if quantity <= 0:
            return "Invalid Quantity"
        if name in self.items:
            self.items[name] += quantity
        else:
            self.items[name] = quantity

    def remove_item(self, name, quantity):
        if name not in self.items:
            return "Item Not Found"
        if quantity <= 0:
            return "Invalid Quantity"
        if self.items[name] < quantity:
            return "Not Enough Stock"
        self.items[name] -= quantity
        if self.items[name] == 0:
            del self.items[name]

    def get_stock(self, name):
        return self.items.get(name, 0)


# -----------------------------
# Assert-based Tests
# -----------------------------
if __name__ == "__main__":
    inv = Inventory()

    # Example Tests
    inv.add_item("Pen", 10)
    assert inv.get_stock("Pen") == 10

    inv.remove_item("Pen", 5)
    assert inv.get_stock("Pen") == 5

    inv.add_item("Book", 3)
    assert inv.get_stock("Book") == 3

    # Extra AI-Generated Tests
    inv.add_item("Pencil", 7)
    assert inv.get_stock("Pencil") == 7

    inv.remove_item("Pencil", 2)
    assert inv.get_stock("Pencil") == 5

    result = inv.remove_item("Eraser", 1)
    assert result == "Item Not Found"

    result = inv.add_item("Marker", 0)
    assert result == "Invalid Quantity"

    result = inv.remove_item("Pen", 20)
    assert result == "Not Enough Stock"

    print("\n✅ All Task 4 Inventory test cases passed successfully!")
