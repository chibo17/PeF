class LinkedList:
    def __init__(self, item):
        self.item = item
        self.next = None
    
    def add(self, item):
        l = LinkedList(item)
        l.next = self
        return l

    def zip(self, other):
        pass




def perm_diff(l):
    pass
    


