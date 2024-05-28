# LeastRecentlyUse_Cache
This is a simple implementation of Least Recently Use Cache with a dictionary and custom Linked List class to achieve the o(1) complexity in the get() and put() method of the cache.

## Class
- LinkedListNode
- LinkedList
    In the context of LRU:
    LinkedList is used to store the order of the key access.
    Attributes:
        - tail: LinkedListNode (the most recently accessed key)
        - head: LinkedListNode (the least recently accessed key)
        - all_nodes: dict (store all the nodes in the linked list)
- LeastRecentlyUsedCache
    Least Recently Used Cache
    Def: Store the most recently accessed key and value pair according to the capacity of the cache. Delete the least recently used key and value according to the queue attribute that indicates the recency of the key.

    Attributes:
        - capacity: int (capacity of the cache)
        - cache: dict (key-value pair, cannot be added more than the capacity)
        - queue: a linked list (store the key in the order of recency, and update the order based on the key access)
    