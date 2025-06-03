class Node:
    def __init__(self,data): #create the nodes i.e., the boxes
        self.data=data  #stores the data value of the node
        self.next=None  #stores address

class linked_list:  #to link the nodes
    def __init__(self):
        self.head=None
        
    def b_insert(self,data):  #insert at the beginning
        newnode=Node(data)  #Node() is called because we need to have data in the form of a structure
        newnode.next=self.head
        self.head=newnode
        
    def e_insert(self,data):  #insert at the end
        newnode=Node(data)
        if self.head is None:
            self.head=newnode
            return
        cur=self.head
        while cur.next:
            cur=cur.next
        cur.next=newnode
    
    def display(self):
        if self.head is None:
            print("empty")
            return
        cur=self.head #if head is not empty, come here
        while cur: #if cur is present,come inside
            print(cur.data,end="->")
            cur=cur.next

obj=linked_list()
obj.b_insert(8)  #Node with data value as 8
obj.b_insert(10)
obj.b_insert(21)
obj.e_insert(36)
obj.display()
