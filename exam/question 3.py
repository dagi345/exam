class queue:
    def __init__(self):
        self.s1=[]
        self.s2=[]
        
    def insert(self, x):
        self.s1.append(x)
        return x
    def remove(self):
        if not self.s2:
            for i in range(len(self.s1)):
                self.s2.append(self.s1.pop())
                
        return self.s2.pop()
        
    def peek(self):
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
                
        return self.s2[-1]

myq=queue()
myq.insert(1)
myq.insert(2)
myq.insert(2)
myq.remove()
myq.peek()







        
            


