class Stack:
    def __init__(self, items=None, limit=100):
        """Initialize the stack with an optional initial list of items and a limit."""
        self.items = items if items is not None else []
        self.limit = limit
        
        if len(self.items) > self.limit:
            raise ValueError("Initial items exceed the stack limit.")

    def isEmpty(self):
        """Check if the stack is empty."""
        return len(self.items) == 0

    def push(self, item):
        """Add an item to the top of the stack."""
        if self.size() < self.limit:
            self.items.append(item)
        else:
            return None  # Handle full stack without raising an error

    def pop(self):
        """Remove and return the item at the top of the stack."""
        if self.isEmpty():
            return None  # Return None instead of raising an error
        return self.items.pop()

    def peek(self):
        """Return the item at the top of the stack without removing it."""
        if self.isEmpty():
            raise IndexError("Stack is empty. Cannot peek.")
        return self.items[-1]

    def size(self):
        """Return the number of items in the stack."""
        return len(self.items)

    def full(self):
        """Check if the stack is full."""
        return len(self.items) == self.limit

    def search(self, item):
        """Search for an item in the stack and return the number of items on top of it."""
        try:
            index = self.items.index(item)  # Find the index of the item in the stack
            return len(self.items) - index - 1  # Return the number of items above it
        except ValueError:
            return -1  # Return -1 if the item is not found
