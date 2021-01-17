from LinkedList import LinkedList

class Queue(LinkedList):
    def Push(self, newNode):
        self.append(newNode)
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