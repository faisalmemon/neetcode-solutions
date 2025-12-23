class ListNode:

    def __init__(self, val, next = None):
        self.val = val
        self.next = next

class LinkedList:

    def __init__(self):
        self.head = None
        return
    
    def get(self, index: int) -> int:
        pointer = self.head
        current_index = 0
        while current_index < index:
            pointer = pointer.next
            if pointer == None:
                return -1
            current_index += 1
        return pointer.val if pointer else -1

    def insertHead(self, val: int) -> None:
        self.head = ListNode(val, self.head)
        
    def insertTail(self, val: int) -> None:
        if self.head == None:
            self.head = ListNode(val)
        else:
            item = self.head
            while item.next != None:
                item = item.next
            item.next = ListNode(val)


    def remove(self, index: int) -> bool:
        dummy = ListNode(0, self.head) # Create a sentinel
        curr = dummy
        i = 0
    
        # We can now treat index 0 exactly like index 1
        while curr and i < index:
             curr = curr.next
             i += 1
        
        if not curr or not curr.next:
            return False
        
        curr.next = curr.next.next
        self.head = dummy.next # Update head in case it was changed
        return True
    
    def getValues(self) -> List[int]:
        result = []
        item = self.head
        while item:
            result.append(item.val)
            item = item.next
        return result
        

