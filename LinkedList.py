class Node:
    def __init__(self, data = None):
        self.data = data
        self.prev = None
        self.next = None
    def set_data(self, data):
        self.data = data
    def get_data(self):
        return self.data
    def set_prev(self, prev):
        self.prev = prev
    def get_prev(self):
        return self.prev
    def has_prev(self):
        return self.prev is not None
    def set_next(self, next):
        self.next = next
    def get_next(self):
        return self.next
    def has_next(self):
        return self.next is not None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.nodeCount = 0
    
    def __del__(self):
        pCur = self.head
        while pCur is not None:
            pPre = pCur
            pCur = pCur.get_next()
            self.nodeCount -= 1
            del(pPre)

    def get_count(self):
        return self.nodeCount
    
    def prepend(self, newNode):
        self.insert_after(None, newNode)
    
    def append(self, newNode):
        self.insert_after(self.tail, newNode)
    
    def insert_after(self, curNode, newNode):
        # If list is empty
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        # Insert after tail
        elif curNode is self.tail:
            self.tail.set_next(newNode)
            newNode.set_prev(self.tail)
            self.tail = newNode
        # Insert at head
        elif curNode is None:
            newNode.set_next(self.head)
            self.head.set_prev(newNode)
            self.head = newNode
        #Insert somewhere in the middle
        else:
            sucNode = curNode.get_next()
            newNode.set_next(sucNode)
            newNode.set_prev(curNode)
            curNode.set_next(newNode)
            sucNode.set_prev(newNode)
        self.nodeCount += 1
    
    def remove(self, curNode):
        sucNode = curNode.get_next()
        predNode = curNode.get_prev()
        if sucNode is not None:
            sucNode.set_prev(predNode)
        if predNode is not None:
            predNode.set_next(sucNode)
        if curNode is self.head: #Removed head
            self.head = sucNode
        if curNode is self.tail: #Removed tail
            self.tail = predNode
        del(curNode)
        self.nodeCount -= 1
    
    def search(self, value):
        ptr = self.head
        while ptr is not None:
            if ptr.get_data() == value:
                return ptr
            ptr = ptr.get_next()
        return ptr
    
    def display(self):
        if self.head is None:
            return False
        ptr = self.head
        while ptr is not None:
            print(ptr.get_data())
            ptr = ptr.get_next()
