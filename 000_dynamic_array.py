class DynamicArray:

    capacity = 0
    storage = []
    
    def __init__(self, capacity: int):
        self.capacity = capacity

    def get(self, i: int) -> int:
        return self.storage[i]

    def set(self, i: int, n: int) -> None:
        storage[i] = n


    def pushback(self, n: int) -> None:
        self.capacity = self.capacity + n

    def popback(self) -> int:
        last_element = self.storage[-1]
        del self.storage[-1]

    def resize(self) -> None:
        self.capacity *= 2

    def getSize(self) -> int:
        return len(self.capacity)
    
    def getCapacity(self) -> int:
        return capacity
