
class SortLinkedList:
    """Sort linked list"""
    
    # ---------------Inner class represente Nodo--------------------------
    class _Node:
        def __init__(self, data) -> None:
            self._data = data
            self._next = None
    # ---------------Inner class represente Nodo--------------------------
    
    def __init__(self, data) -> None:
        self.head = self._Node(data)
        
    def print_list(self):
        s =""
        if self.head is not None:
            a = self.head
            while a:
               s += str(a._data) + " -> "
               a = a._next
            return s
        else:
            return "Lis is empty"
                