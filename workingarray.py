import os
from time import time
from style import Style
from random import randint, choice

def createArray(m, n):
    array = [m] * n
    return array

def createArraySquence(n):
    array = [x for x in range(n)]
    return array

def createArrayRandom(n):
    squence = [x for x in range(n)]
    array = []
    for _ in range(n):
        e = randint(0, n)
        array.append(e)
    return array

def insertatbegin(array, e):
    array.insert(0,e)    
    return array

def insertatend(array, e):
    array.append(e)  
    return array

def remove(array, elem):
    try:
        return array.remove(elem)
    except Exception as e:
        print(f"value element no in the list {elem}")

def countduplicate(array, elem):
    if(len(array) == 0):
        return 0
    count = 0
    for e in array:
        if (e == elem):
            count += 1
    return count

def removeduplicate(array):
    return list(dict.fromkeys(array))

def main() -> None:
    os.system("clear")
    start_time = time()
    
    # array = createArray(None,4)
    # array = createArraySquence(10)
    array = createArrayRandom(4)
    
    print(f"count: {len(array)}")
    
    for i in array:
        print(i,end=", ")   
    
    insertatbegin(array, -1)
    insertatend(array, 5)
    
    print()
    
    for i in array:
        print(i,end=", ") 

    print()
    print(f"count: {len(array)}")
    
    remove(array, 2)
    
    print()
    
    for i in array:
        print(i,end=", ") 

    print()
    print(f"count: {len(array)}")
    
    print()
    print(f"duplicate element: {countduplicate(array, 3)}")
    
    print()
    
    for i in removeduplicate(array):
        print(i,end=", ") 
    
    print()
    
    end_time = time()
    elapsed = end_time - start_time
    print(Style.WHITE)

    print(f"duration of the execution {elapsed:.2f}")


if __name__ == "__main__":
    main()
