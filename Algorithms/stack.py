class queue:
    def __init__(self):
        self.queue = list()

    def push(self,dataval):     
        if dataval not in self.queue:
            self.queue.insert(0,dataval)
            return True
        return False

    def front(self):
        if(self.size()>0):
            return self.queue[0]
    
    def pop(self):
        if(self.size()>0):
            self.queue.pop(0)
            return True
        return False

    def size(self):
      return len(self.queue)

q = queue()
q.push("Mon")
q.push("Tue")
q.push("Wed")
print(q.size())
print(q.front())
print(q.pop())
print(q.front())
