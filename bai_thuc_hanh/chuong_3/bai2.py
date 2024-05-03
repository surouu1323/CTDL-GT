class Node:
    def __init__(self,HeSo,SoMu):
        self.HeSo = HeSo
        self.SoMu = SoMu
        self.next = None
        
class PhuongThuc:
    def __init__(self):
        self.head = None
    
    def Them(self,new_HeSo,new_SoMu):
        new_node = Node(new_HeSo,new_SoMu)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            if last.next.SoMu < new_node.SoMu:
                last.next = new_node
                return
            last = last.next
        last.next = new_node
        
    def RutGon(self):
        goc = self.head
        pre_goc = goc
        while goc:
            search = goc.next
            while search:
                if search.SoMu == goc.SoMu:
                    goc.HeSo += search.HeSo
                    goc.next = search.next
                search = search.next
            if goc.HeSo == 0:
                if goc.next is None:
                    pre_goc.next = None
                elif goc == self.head:
                    self.head = goc.next
                    pre_goc = self.head   
                else:
                    pre_goc.next = goc.next
                goc = pre_goc
            else:
                goc = goc.next

        
    def Print(self):
        temp = self.head
        while temp:
            
            if temp.HeSo > 0:
                dau = '+'
            elif temp.HeSo < 0:
                dau = '-'
            else:
                dau = '-'
            if temp.HeSo == 1 or temp.HeSo == -1:
                so = None
            else:
                so = abs(temp.HeSo)
            
            
            dathuc = [dau if temp != self.head or temp.HeSo < 0 else '','' if so is None else so,'x','^' if temp.SoMu else '', temp.SoMu if temp.SoMu else '']
            dathuc_string = ''.join([str(m) for m in dathuc])
            print(dathuc_string, end=' ')
            temp = temp.next

        
dathuc = PhuongThuc()
dathuc.Them(-2,2)
dathuc.Them(2,2)
dathuc.Them(-2,2)
dathuc.Them(3,1)
dathuc.Them(-3,1)
dathuc.Them(-3,0)
dathuc.Print()
print("\n")
dathuc.RutGon()
dathuc.Print()