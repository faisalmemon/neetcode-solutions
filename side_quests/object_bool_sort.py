# The task is to keep the relative order of the True items the same
# but move the False items to the Front.

class Item:
    def __init__(self, char: str, result: bool):
        self.char = char
        self.result = result

    def dump_item(self):
        print(f'Data: {self.char} Bool: {self.result}')

class DataStore:
    def __init__(self, items=None):
        self.items = items if items is not None else []

    def add_item(self, item: Item):
        self.items.append(item)

    def dump_items(self):
        for item in self.items:
            item.dump_item()

    def reorder(self):
        high = len(self.items) - 1
        if high == -1 or high == 0:
            return
        low = high - 1
        while low >= 0:
            if self.items[high].result:
                high -= 1
                low -= 1
                continue
            if not self.items[low].result:
                low -= 1
                continue
            self.items[low], self.items[high] = self.items[high], self.items[low]
            low -= 1
            high -= 1

if __name__ == "__main__":
    store = DataStore()
    store.add_item(Item('h', False))
    store.add_item(Item('e', False))
    store.add_item(Item('l', True))
    store.add_item(Item('l', False))
    store.add_item(Item('o', True))
    store.add_item(Item('w', True))
    store.add_item(Item('o', False))
    store.add_item(Item('r', False))
    store.add_item(Item('l', True))
    store.add_item(Item('d', False))
    store.dump_items()

    print("Re-ordering\n\n")
    store.reorder()
    store.dump_items()