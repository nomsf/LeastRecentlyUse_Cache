import LinkedListUtil

class LeastRecentlyUsedCache:
    '''
    Least Recently Used Cache
    Def: Store the most recently accessed key and value pair according to the capacity of the cache. Delete the least recently used key and value according to the queue attribute that indicates the recency of the key.

    Attributes:
        - capacity: int (capacity of the cache)
        - cache: dict (key-value pair, cannot be added more than the capacity)
        - queue: a linked list (store the key in the order of recency, and update the order based on the key access)
    
    '''
    def __init__(self, capacity: int):
        try:
            if capacity <= 0:
                raise ValueError("Capacity must be greater than 0")
            self.capacity = capacity
            self.cache = {}
            self.queue = LinkedListUtil.LinkedList()

        except ValueError as e:
            raise e
    
    def print(self):
        print("Capacity: ", self.capacity)
        print("Cache: ", self.cache)
        print("Queue: ", end = " ")
        self.queue.print()
        print("Queue Dict: ", self.queue.all_nodes)
        print("Queue Head: ", self.queue.head)
        print("Queue Tail: ", self.queue.tail)
        
    def get(self, key: int) -> int:
        try:
            if key in self.cache:
                node = self.queue.find(key)
                self.queue.remove(node)
                self.queue.append(key)
                return self.cache[key]
            return -1
        except Exception as e:
            raise e
        
    def put(self, key : int, value : int) -> None:
        try:
            if len(self.cache) == self.capacity:
                del self.cache[self.queue.head.value]
                self.queue.remove(self.queue.head) # remove the least recently used key
            self.cache[key] = value
            self.queue.append(key)
        except Exception as e:
            raise e
    


        

