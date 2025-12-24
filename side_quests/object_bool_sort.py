# The task is to keep the relative order of the True items the same
# but move the False items to the Front.

class Item:
    def __init__(self, char: str, result: bool):
        self.char = char
        self.result = result

    def dump_item(self):
        print(f'Data: {self.char} Bool: {self.result}')
    
    def __repr__(self):
        return f"Item('{self.char}', {self.result})"

class DataStore:
    def __init__(self, items=None):
        self.items = items if items is not None else []

    def add_item(self, item: Item):
        self.items.append(item)

    def dump_items(self):
        for item in self.items:
            item.dump_item()

    def reorder(self):
        """
        Reorders items in-place: False items first, True items last.
        Maintains relative order of True items.
        Time: O(n), Space: O(1)
        """
        if len(self.items) <= 1:
            return
        
        # Two-pointer approach: work backwards, swapping True items at 'low'
        # with False items at 'high' to partition False items to the front
        high = len(self.items) - 1
        low = high - 1
        
        while low >= 0:
            if self.items[high].result:
                # high points to True, skip it
                high -= 1
                low -= 1
            elif not self.items[low].result:
                # low points to False, skip it
                low -= 1
            else:
                # low=True, high=False: swap to move False item forward
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