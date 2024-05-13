class stack:
    def __init__(self):
        self.stack=[]
    
    
    def isempty(self):
        return not bool(self.stack)
    
    def push(self, element):
        self.stack.append(element)
    
    def pop(self):
        if len(self.stack)==0:
            return "the stack is empty"
        return self.stack.pop()
    def size(self):
        if len(self.stack)==0:
            return "the stack is empty"
        
        return len(self.stack)
    
    def peek(self):
        if self.isempty():
            return "the stack is empty"
        return self.stack[-1]
    def printmystack(self):
        for i in self.stack:
            print(i, end=' ')
    
mystack=stack()
print(mystack.isempty())
mystack.push(5)
mystack.push(6)
mystack.push(7)
mystack.push(8)
mystack.pop()
mystack.pop()
print(mystack.size())
print(mystack.peek())

mystack.printmystack()






        
        
        