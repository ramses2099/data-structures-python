import os
from time import time
from style import Style
from hashtable import HashTable

def main() -> None:
    os.system("clear")
    start_time = time()
    
    t = HashTable()
    t["item 1"] = 30
    t["item 2"] = 31
    t["item 3"] = 32
    
    print(t.arr)
    del t["item 2"]
    
    print(Style.GREEN)
    print(t.arr)
    

    end_time = time()
    elapsed = end_time - start_time
    print(Style.WHITE)

    print(f"duration of the execution {elapsed:.2f}")


if __name__ == "__main__":
    main()
