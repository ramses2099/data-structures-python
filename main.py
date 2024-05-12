import os
from time import time
from arraystack import ArrayStack
from linkedqueue import LinkedQueue

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
  lqueue = LinkedQueue()
  lqueue.enqueue(1)
  lqueue.enqueue(2)
  lqueue.enqueue(3)
  lqueue.enqueue(4)
  
  for i in range(lqueue.__len__()):
    print(f"element out queue {lqueue.dequeue()}")
  
  print(f"list empty {lqueue.is_empty()}")
     
  end_time = time()
  elapsed = end_time - start_time
  print()
  print(f"duration of the execution {elapsed:.2f}")
      
if __name__ == "__main__":
    main()