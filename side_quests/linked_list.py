class ListNode:
    def __init__(self, data=0, next_node=None):
        self.data = data
        self.next = next_node

    def search_list(self, L, key):
        while L and L.data != key:
            L = L.next
        return L

    def insert_after(self, node, new_node):
        new_node.next = node.next
        node.next = new_node
    
    def delete_after(self, node):
        node.next = node.next.next
        
