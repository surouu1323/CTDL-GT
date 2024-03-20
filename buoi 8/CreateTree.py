class TreeNode:
    def _init_(self, data, children = []):
        self.data = data
        self.children = children
        
    def _str_(self, level=0):
        ret = " "* level + str(self.data) + "\n"
        for child in self.children:
            ret += child._str_(level + 1)
        return ret
    
    def addChild(self, TreeNode):
        self.children.append(TreeNode)
        
tree = TreeNode('Drinks', [])
cold = TreeNode('Cold', [])
hot = TreeNode('Hot', [])
tree.addChild(cold)
tree.addChild(hot)
tea = TreeNode('Tea', [])
coffee = TreeNode('Coffee', [])
cola = TreeNode('Cola', [])
fanta = TreeNode('Fanta', [])
cold.addChild(cola)
cold.addChild(fanta)
hot.addChild(tea)
hot.addChild(coffee)
print(tree)