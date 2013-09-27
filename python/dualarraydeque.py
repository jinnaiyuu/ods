'''
An array-based list implementation with O(1+min{i,n-i}) amortized update time.

This running time is achieved by gluing together two ArrayStacks,
called front and back, so that they are back to back.

Items are redistributed even between front and back whenever one is more than
three times the size of the other.
'''

from arraystack import ArrayStack

from arraybasedlist import ArrayBasedList

class DualArrayDeque(ArrayBasedList):
    def __init__(self):
        self.front = ArrayStack()
        self.back = ArrayStack()
    
    def get(self, i):
        if i < self.front.size():
            return self.front.get(self.front.size()-i-1)
        else:
            return self.back.get(i-self.front.size())
    
    def set(self, i, x):
        if i < self.front.size():
            return self.front.set(front.size()-i-1, x)
        else:
            return self.back.set(i-self.front.size(), x)
    
    def add(self, i, x):
        if i < self.front.size():
            self.front.add(self.front.size()-i, x)
        else:
            self.back.add(i-self.front.size(), x)
        self._balance()

    def remove(self, i):
        if i < self.front.size():
            x = self.front.remove(self.front.size()-i-1)
        else:
            x = self.back.remove(i-self.front.size())
        self._balance()
        return x

    def _balance(self):
        n = self.size()
        mid = n//2
        if 3*self.front.size() < self.back.size() \
           or 3*self.back.size() < self.front.size():
            f2 = ArrayStack()
            for i in range(mid):
                f2.add(i, self.get(mid-i-1))
            b2 = ArrayStack()
            for i in range(n-mid):
                b2.add(i, self.get(mid+i)) 
            self.front = f2
            self.back = b2

    def size(self):
        return self.front.size() + self.back.size()        

    def clear(self):
        self.front.clear()
        self.back.clear()

    def _debug_str(self):
        return str([self.front.get(self.front.size()-i-1) \
                    for i in range(self.front.size())]) \
               + str([self.back.get(i) for i in range(self.back.size())])

