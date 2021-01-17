from LinkedList import LinkedList

class Stack(LinkedList):
    def Push(self, newNode):
        self.prepend(newNode)
    def Pop(self):
        data = self.head.data
        self.remove(self.head)
        return data
    def Peek(self):
        return self.head.data
    def IsEmpty(self):
        return self.head is None
    def GetLength(self):
        return self.get_count()
