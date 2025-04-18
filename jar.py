class Jar:
    def __init__(self, capacity=12):
        if not isinstance(capacity, int):
            raise TypeError("Capacity must be an integer.")
        if capacity < 0:
            raise ValueError("Capacity must be a non-negative integer.")
        self._capacity = capacity  # Store max capacity
        self._size = 0  # Current number of cookies (starts empty)

    def __str__(self):
        return "🍪" * self._size  # Returns 🍪 repeated `size` times

    def deposit(self, n):
        if not isinstance(n, int) or n < 0:
            raise ValueError("Must deposit a non-negative integer.")
        if self._size + n > self._capacity:
            raise ValueError("Not enough space in the jar.")
        self._size += n

    def withdraw(self, n):
        if not isinstance(n, int) or n < 0:
            raise ValueError("Must withdraw a non-negative integer.")
        if self._size - n < 0:
            raise ValueError("Not enough cookies in the jar.")
        self._size -= n

    @property
    def capacity(self):
        return self._capacity  # Return max capacity

    @property
    def size(self):
        return self._size  # Return current number of cookies
