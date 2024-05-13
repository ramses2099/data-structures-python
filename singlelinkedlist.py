class SingleLinkedList:
    """FIFO queue implementation using a singly liked list for storage"""
    #--------------------------- nested _Node class----------------------
    class _Node:
        """Lightweight nonpublic class for storing a singly linked node"""
        __slots__='_data', '_next'
        
        def __init__(self, data) -> None:
            self._data = data
            self._next = None
     #--------------------------- nested _Node class----------------------
     
    def __init__(self) -> None:
        self.head = None
        
    def insertion_at_begin(self, data):
        """Insert node at begining of the linked list"""
        nb = self._Node(data)
        nb._next = self.head
        self.head = nb
        
    def insertion_at_end(self, data):
        """Insert node at end of the linked list"""
        ne = self._Node(data)
        a = self.head
        while a._next is not None:
            a = a._next
        a._next = ne
    
    def insertion_at_specified_node(self, position, data):
        """Insert Node at specified position"""
        npn = self._Node(data)
        a = self.head
        for i in range(1, position-1):
            a = a._next
        npn._next = a._next
        a._next = npn
    
    def delete_at_specified_node(self, position):
        """Delete Node at specified position of the linked list"""
        prev = self.head
        a = self.head._next
        for i in range(1, position - 1):
            a = a._next
            prev = prev._next
        prev._next = a._next
        a._next = None 
        return a
        
    def delete_at_begining(self):
        """Delete Node at begining of the linked list"""
        a = self.head
        self.head = a._next
        a._next = None
        return a
        
    def delete_at_end(self):
        """Delete Node at end of the linked list"""
        prev = self.head
        a = self.head._next
        while a._next is not None:
            a = a._next
            prev = prev._next
        prev._next = None
        return a
        
    def traversal(self):
        if self.head is None:
            raise Exception("singly linked list is empty")
        else:
            a = self.head
            while a is not None:
                print(a._data, end="->")
                a=a._next