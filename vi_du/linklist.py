class Node:
    def __init__(self,HeSo,SoMu):
        self.HeSo = HeSo
        self.SoMu = SoMu
        self.next = None
        
class PhuongThuc:
    def __init__(self):
        self.head = None
    
    def them(self,new_HeSo,new_SoMu):
        new_node = Node(new_HeSo,new_SoMu)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            if last.next.SoMu < new_node.SoMu:
                temp = last.next
                last.next = new_node
                new_node.next = temp
                return
            last = last.next
        last.next = new_node
        
    def print(self):
        temp = self.head
        while temp:
            dathuc = [temp.HeSo if temp.HeSo > 1 else "","x^",temp.SoMu,'+' if temp.next else ""]
            dathuc_string = ''.join([str(m) for m in dathuc])
            print(dathuc_string, end=' ')
            temp = temp.next
            
dathuc = PhuongThuc()
dathuc.them(1,2)
dathuc.them(4,0)
dathuc.them(3,1)

dathuc.print()