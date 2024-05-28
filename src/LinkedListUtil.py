import LinkedListNode as lld

class LinkedList:
    '''
    In the context of LRU:
    LinkedList is used to store the order of the key access.
    Attributes:
        - tail: LinkedListNode (the most recently accessed key)
        - head: LinkedListNode (the least recently accessed key)
        - all_nodes: dict (store all the nodes in the linked list)
    '''
    def __init__(self):
        self.head : lld.LinkedListNode = None
        self.tail : lld.LinkedListNode = None
        self.all_nodes = {}

    def __iter__(self):
        current = self.head
        while current:
            yield current
            current = current.next

    def find(self, value):
        return self.all_nodes[value]
    
    def remove(self, node : lld.LinkedListNode):
        if node == self.head:
            self.head = node.next
        if node == self.tail:
            self.tail = node.prev
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        del self.all_nodes[node.value]

    def append(self, value : int):
        if(value in self.all_nodes):
            node = self.all_nodes[value]
            self.remove(node)
        
        node = lld.LinkedListNode(value)
        
        if(len(self.all_nodes) == 0):
            self.head = node
            self.tail = node
            self.all_nodes[value] = node
            return
        
        self.all_nodes[value] = node
        
        self.tail.next = node
        node.prev = self.tail
        self.tail = node

    def print(self):
        current = self.head
        while current:
            print(current.value, end = ",")
            current = current.next
        print()