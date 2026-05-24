class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None
    
class LRUCache:
    def __init__(self, capacity: int):
        self.cache = dict()
        self.capacity = capacity
        self.currentSize = 0
        self.head = Node(None, None) # Most recently used
        self.tail = Node(None, None) # Least recently used
        self.head.next = self.tail 
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.cache:
            # put node with this key in first place
            temp = self.head
            while temp.next.key != key:
                temp = temp.next
            thisNode = temp.next
            temp.next = temp.next.next
            temp.next.prev = temp
            firstNode = self.head.next
            self.head.next = thisNode
            thisNode.next = firstNode
            thisNode.prev = self.head
            firstNode.prev = thisNode
            return self.cache[key]
        return -1
        
        

    def put(self, key: int, value: int) -> None:
        newNode = Node(key, value)
        if key in self.cache:
            self.cache[key] = value
            temp = self.head
            while temp.next.key != key:
                temp = temp.next

            # remove it from its original position
            nextToNextNode = temp.next.next
            temp.next = nextToNextNode
            nextToNextNode.prev = temp

            # add it in beginning
            firstNode = self.head.next
            self.head.next = newNode
            newNode.next = firstNode
            newNode.prev = self.head
            firstNode.prev = newNode
            
        elif self.capacity == self.currentSize:
            # remove from last
            lastNode = self.tail.prev
            secondLastNode = lastNode.prev
            secondLastNode.next = self.tail
            self.tail.prev = secondLastNode

            # insert in beginning
            firstNode = self.head.next
            self.head.next = newNode
            newNode.next = firstNode
            newNode.prev = self.head
            firstNode.prev = newNode

            # add in cache
            self.cache[key] = value
            del self.cache[lastNode.key]
        else:
            # insert in beginning
            firstNode = self.head.next
            self.head.next = newNode
            newNode.next = firstNode
            newNode.prev = self.head
            firstNode.prev = newNode

            # add in cache
            self.cache[key] = value

            # increase size
            self.currentSize += 1
        

        

    


        
