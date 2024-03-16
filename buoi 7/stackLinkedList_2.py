class Node:
    def _init_(self, value = None):
        self.value = value
        self.next = next
        
class LinkedList:
    def _init_(self):
        self.head = None
class Stack:
    def _init_(self):
        self.LinkedList = LinkedList()
    def isEmpty(self):
        if self.LinkedList.head == None:
            return True
        else:
            return False
    def push(self, value):
        node = Node(value)
        node.next = self. LinkedList.head
        self.LinkedList.head = node
        
        
customStack = Stack()
customStack.push(1)
customStack.push(2)
customStack.push(3)
print(customStack)
