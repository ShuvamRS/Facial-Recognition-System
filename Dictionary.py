from LinkedList import Node
from Stack import Stack
from BST import BinarySearchTree as BST


class Dictionary_node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
    def __eq__(self, other):
        return self.key == other
    def __lt__(self, other):
        try:
            return other.key < self.key
        except:
            return other < self.key        
    def __gt__(self, other):
        try:
            return other.key > self.key
        except:
            return other > self.key
    def __str__(self):
        items = (self.key, self.value)
        return str(items)


class Dictionary:
    def __init__(self, items = None):
        self.bst = BST()
        if items is not  None:
            for i in items:
                self.__setitem__(i[0], i[1])
    def __setitem__(self, key, value):
        self.bst.insert(Dictionary_node(key, value))
    def __getitem__(self, key):
        return self.bst.search(key).value
    def __delitem__(self,key):
        self.bst.remove(key)
    def __str__(self):
        container = []
        for i in self:
            container.append((i.key, i.value))
        return str(container)
    def __iter__(self):
        if self.bst.root is None:
            return
        stack = Stack()
        stack.Push(Node(self.bst.root))

        while stack.IsEmpty() is False:
            temp = Stack()

            while stack.IsEmpty() is False:
                temp.Push(Node(stack.Pop()))
            while temp.IsEmpty() is False:
                node = temp.Pop()
                yield node.get_data()
                if node.get_left() is not None:
                    stack.Push(Node(node.get_left()))
                if node.get_right() is not None:
                    stack.Push(Node(node.get_right()))
    def keys(self):
        container = []
        for i in self:
            container.append(i.key)
        return container
    def values(self):
        container = []
        for i in self:
            container.append(i.value)
        return container
    def items(self):
        container = []
        for i in self:
            container.append((i.key, i.value))
        return container

    def __zip__(self, *iterables):
        '''
        Taken from https://docs.python.org/3.3/library/functions.html
        '''
        sentinel = object()
        iterators = [iter(it) for it in iterables]
        while iterators:
            for it in iterators:
                elem = next(it, sentinel)
                if elem is sentinel:
                    return
            yield ((elem.key, elem.value))
