class Node:
    def __init__(self, x, l, r):
        self.x = x
        self.l = l
        self.r = r
        self.rh= rwys(r) + 1 
def rwys(d):
    if d:
        return d.rh
    else:
        return 0
def join(d1, d2):
    if d1 is None:
        return d2
    elif d2 is None:
        return d1
    else:
        smaller, bigger = (d1, d2) if d1.x < d2.x else (d2,d1)
        smaller.r = join(smaller.r, bigger)
        if rwys(smaller.r) > rwys(smaller.l):
            smaller.r, smaller.l = smaller.l, smaller.r
        smaller.rh =  rwys(smaller.r)+1
        return smaller
def Pqueue:
    def __init__(self):
        self.root = None
    def add(self, x):
        self.root = join(self.root, Node(x,None,None))
    def getMin(self):
        self.root.x
    def removeMin(self): 
        self.root= join(self.root.l, self.root.r)
    def isEmpty():
        return not self.root



p = Pqueue()
p.add(17)
p.add(18)
print(p.getMin())
p.removeMin()
