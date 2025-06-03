class stack:
    def __init__(self):
        self.box=[]
    def push(self,data):
        self.box.append(data)
                               
    def display(self):
        if len(self.box)==0:
            print("empty")
            return
        for i in self.box[::-1]:
            print(i,end=" ")
            
    def pop(self):
        if len(self.box)==0:
            print("empty")
            return
        self.box.pop()
            
    def peek(self):
        if len(self.box) == 0:
            print("empty")
            return
        print(self.box[-1])
                 
stack1=stack()   #object1  #size of stack=3
stack1.push(18)   #18 = data
stack1.push(7)
stack1.push(3)
stack1.push(34)   #stack will be overflow
stack1.display()  #display the data
stack1.peek() #display the top element
stack1.pop()
stack1.display()   
