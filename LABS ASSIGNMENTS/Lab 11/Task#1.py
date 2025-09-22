class Stack:
    """
    A simple stack implementation using Python list.
    
    Methods:
        push(item): Add an item to the top of the stack.
        pop(): Remove and return the top item of the stack.
        peek(): Return the top item without removing it.
        is_empty(): Return True if the stack is empty, else False.
        display(): Print the current contents of the stack.
    """
    def __init__(self):
        self._data = []

    def push(self, item):
        """Push an item onto the stack."""
        self._data.append(item)

    def pop(self):
        """Pop the top item off the stack. Raises IndexError if empty."""
        if not self._data:
            raise IndexError("pop from empty stack")
        return self._data.pop()

    def peek(self):
        """Return the top item without removing it. Raises IndexError if empty."""
        if not self._data:
            raise IndexError("peek from empty stack")
        return self._data[-1]

    def is_empty(self):
        """Check if the stack is empty."""
        return len(self._data) == 0

    def display(self):
        """Display the contents of the stack (top shown last)."""
        print("Stack contents:", self._data)


# ---------- TEST CASES ----------
if __name__ == "__main__":
    s = Stack()

    print("\n--- Stack Operations Demo ---")

    # Test 1: Stack should be empty initially
    assert s.is_empty() == True
    s.display()

    # Test 2: Push items
    s.push(10)
    s.push(20)
    s.push(30)
    s.display()  # Expect [10, 20, 30]
    assert s.peek() == 30

    # Test 3: Pop one element
    popped = s.pop()
    print("Popped:", popped)
    s.display()  # Expect [10, 20]
    assert popped == 30

    # Test 4: Peek top element
    print("Top element:", s.peek())
    assert s.peek() == 20

    # Test 5: Pop remaining
    s.pop()
    s.pop()
    s.display()  # Expect []
    assert s.is_empty() == True

    print("\n✅ All Stack test cases passed successfully!")
