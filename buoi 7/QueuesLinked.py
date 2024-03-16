class Node:
    __slots = '_element', '_next'
    
    def __init__(self, element, next):
        self._element = element
        self._next = next
        
class QueuesLinked:
    def _init__(self):
        self._front = None
        self._rear = None
        self._size = 0
    def _len_(self):
        return self._size
    def isempty(self): 
        return self._size == 0