class stack:
    def __init__(self,size):   #constructor as obj1 is created
        self.size=size
        self.box=[0]*self.size  #stack created initially with all elements as 0 
        self.top=-1    #index of top initially = -1
        
    def push(self,data):
        if self.top+1 == self.size:   #self.top=3; 3+1=4; size of stack=3
            print("Overflow")
            return 
        self.top+=1
        self.box[self.top]=data    #data = 18,7,3
        
    def display(self):
        if self.top == -1:   #stack is empty
            print("Underflow")
            return
        for i in range(self.top,-1,-1):  #start from top till 0th index in reverse direction
            print(self.box[i],end=" ")
    
    def pop(self):
        if self.top == -1:
            print("Underflow")
            return
        self.top-=1
        
    def peek(self):
        if self.top == -1:
            print("Underflow")
            return
        print()
        print(self.box[self.top])
        
stack1=stack(3)   #object1  #size of stack=3
stack1.push(18)   #18 = data
stack1.push(7)
stack1.push(3)
stack1.push(34)   #stack will be overflow
stack1.display()  #display the data
stack1.peek() #display the top element
stack1.pop()
stack1.display()
