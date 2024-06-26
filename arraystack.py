class Empty(Exception):
    """Error attempting to access an element from an empty container"""
    pass

class ArrayStack:
    """LIFO Stack implementation using a Python lis as underlying storage"""

    def __init__(self) -> None:
        """Create a empty stack"""
        self._data = []

    def __len__(self):
        """Return the number of elements in the stack"""
        return len(self._data)
    
    def is_empty(self):
        """Return True if the stack is empty"""
        return len(self._data) == 0
    
    def push(self, e):
        """Add element e to the top of the stack"""
        self._data.append(e)
        
    def pop(self):
        """Remove and return the element form the top of th stack (i.e., LIFO)
        
        Raise Empty exception if the stack is empty
        """
        if self.is_empty():
            raise Empty("Stack is empty")
        return self._data.pop() 
    
    def top(self):
        """Return (but do not remove) the element at the top of the stack
        
        Raise Empty exception if the stack is empty
        """
        if self.is_empty():
            raise Empty("Stack is empty")
        return self._data[-1] #Last item in the list
    
    
    
