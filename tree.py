class Tree:
    
    #-----------------Child Private class------------------------------------
    class _Node:
        def __init__(self, data) -> None:
            self._left = None
            self._right = None
            self._data = data
   #-----------------Child Private class------------------------------------
   
    def __init__(self):
      self.head = None
   
    def insert(self, data):
       if self.head is None:
           self.head = self._Node(data)
       else:
           if self.head._data < data:
               if self.head._left is None:
                   self.head._left = self._Node(data)
               else:
                   self.insert(data)
           else:
               if self.head._right is None:
                   self.head._right = self._Node(data)
               else:
                   self.insert(data) 