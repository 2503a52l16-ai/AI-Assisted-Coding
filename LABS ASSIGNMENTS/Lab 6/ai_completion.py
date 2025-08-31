
class Product:
    """Represents a product using a dictionary for attributes."""

    def __init__(self, name: str, price: float, quantity: int):
        self.info = {
            "name": name,
            "price": price,
            "quantity": quantity
        }

    def calculate_value(self) -> float:
        """Calculate and return total value of the product."""
        return self.info["price"] * self.info["quantity"]

    def __str__(self):
        """Readable string for printing product details."""
        return f"{self.info['name']} ({self.info['quantity']} units @ {self.info['price']})"


class Warehouse:
    """Represents a warehouse managing multiple products."""

    def __init__(self):
        self.stock = []

    def add_product(self, product: Product):
        """Add a new product to the warehouse."""
        self.stock.append(product)

    def remove_product(self, product_name: str):
        """Remove a product from the warehouse by name."""
        self.stock = [p for p in self.stock if p.info["name"] != product_name]

    def total_value(self) -> float:
        """Return the total value of all products in stock."""
        return sum(p.calculate_value() for p in self.stock)

    def list_products(self):
        """Prints a list of all products in stock."""
        if not self.stock:
            print("No products in warehouse.")
        else:
            for product in self.stock:
                print(product)


# Example usage
if __name__ == "__main__":
    p1 = Product("Tablet", 300.0, 7)
    p2 = Product("Headphones", 50.0, 20)
    p3 = Product("Monitor", 200.0, 5)

    warehouse = Warehouse()
    warehouse.add_product(p1)
    warehouse.add_product(p2)
    warehouse.add_product(p3)

    print("Products in warehouse:")
    warehouse.list_products()
    print("Total value:", warehouse.total_value())

    # Example of removing a product
    warehouse.remove_product("Headphones")
    print("\nAfter removing Headphones:")
    warehouse.list_products()
    print("Total value:", warehouse.total_value())
