
class TreeNode:
    def __init__(self,value):
        self.left = None
        self.right = None
        self.value = value
        
    def insert(self,value):
        if value < self.value:
            if self.left is None:
                self.left = TreeNode(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = TreeNode(value)
            else:
                self.right.insert(value)
    def inorder(self):
        if self.left:
            self.left.inorder()
        print(self.value)
        if self.right:
            self.right.inorder()    
            
r = TreeNode(50)
r.insert(30)
r.insert(20)
r.insert(40)
r.insert(70)
r.insert(60)
r.insert(80)


r.inorder()