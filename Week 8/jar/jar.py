class Jar:
    def __init__(self, capacity=12):
        if int(capacity) < 0:
            raise ValueError
        else:
            self._capacity = int(capacity)
            self._size = int(0)

    def __str__(self):
        return("🍪" * self._size)

    def deposit(self, n):
        if int(n) < 0:
            raise ValueError
        elif (int(n) + self._size) > self._capacity:
            raise ValueError("Exceeds capacity")
        else:
            self._size += n

    def withdraw(self, n):
        if int(n) < 0:
            raise ValueError
        elif int(n) > self._size:
            raise ValueError("Insufficient cookies")
        else:
            self._size -= n

    @property
    def capacity(self):
        return int(self._capacity)

    @property
    def size(self):
        return int(self._size)


if __name__ == "__main__":
    main()
