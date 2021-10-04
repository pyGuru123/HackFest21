#implementation of stack 
class Stack:
    def __init__(self):
        self.stack = list()

    def push(self,dataval):     
        if dataval not in self.queue:
            self.stack.insert(0,dataval)
            return True
        return False

    def top(self):
        if(self.size()>0):
            return self.stack[0]
    
    def pop(self):
        if(self.size()>0):
            self.stack.pop(0)
            return True
        return False

    def size(self):
      return len(self.stack)

s = Stack()
s.push("Mon")
s.push("Tue")
s.push("Wed")
print(s.size())
print(s.front())
print(s.pop())
print(s.front())
