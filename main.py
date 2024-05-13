import os
from time import time
from arraystack import ArrayStack
from singlelinkedlist import SingleLinkedList
from doublylinkedlist import DoublyLinkedList

A = [1,2,6,6]
B = [4,5,6]
C = [7,6,9]

def prefix_average(S):
  """REturn list such that, for all j, A[j] equals average of S[0], ..., S[j]."""
  n = len(S)
  A = [0] * n
  for j in range(n):
    total = 0
    for i in range(j + 1):
      total += S[i]
    A[j] = total / (j+1)
  return A

def disjoint1(A, B, C):
  """Return True if there is no element common to all three lists"""
  for a in A:
    for b in B:
      if a == b:
        for c in C:
          if a == c:
            return False
  return True

def unique1(S):
  """Return True if there are no duplicate elements in sequence S."""
  for j in range(len(S)):
    for k in range(j+1, len(S)):
      if S[j] == S[k]:
        return False
  return True     

def unique2(S):
  """Return True if there are no duplicate elements in sequence S."""
  temp = sorted(S)
  for j in range(1, len(temp)):
      if S[j-1] == S[j]:
        return False
  return True     

def is_matched(expr):
  """Return True if all delimiters are properly match; False otherwise"""
  lefty = "({["
  righty = ")}]"
  S = ArrayStack()
  for c in expr:
    if c in lefty:
      S.push(c)
    elif c in righty:
      if S.is_empty():
        return False
      if righty.index(c) != lefty.index(S.pop()):
        return False
  return S.is_empty()

def main() -> None:
  os.system("clear")
  start_time = time()
  #  code here
  dblll = DoublyLinkedList()
  nd1 = DoublyLinkedList._Node(1)
  dblll.head = nd1
  nd2 = DoublyLinkedList._Node(2)
  nd1._next = nd2
  nd2._prev = nd1  
  nd3 = DoublyLinkedList._Node(3)
  nd2._next = nd3
  nd3._prev = nd2 
  nd4 = DoublyLinkedList._Node(4)
  nd3._next = nd4
  nd4._prev = nd3
  dblll.insertion_at_begin(0)
  dblll.insertion_at_end(5)
  dblll.insertion_at_begin(-2)
  
  dblll.insertion_at_specified_node(1,-1)
  
  dblll.forward_traversal()
  print()
  dblll.backward_traversal() 
  
  dblll.delete_at_begining()
  print()
  dblll.forward_traversal()
  print()
  dblll.backward_traversal() 
     
  end_time = time()
  elapsed = end_time - start_time
  print()
  print(f"duration of the execution {elapsed:.2f}")
      
if __name__ == "__main__":
    main()