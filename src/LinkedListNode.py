class LinkedListNode:
    '''
     - value: keys of LRU cache
    '''
    def __init__(self, value):
        self.value : int = value
        self.next : LinkedListNode = None
        self.prev : LinkedListNode = None


    def __repr__(self):
        return str(self.value)