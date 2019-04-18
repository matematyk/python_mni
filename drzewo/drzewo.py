class Node():
    def __int__(self, x, l, r):
        self.x = x
        self.l = l
        self.r = r 
        
def wstaw(x, tree):
    if tree is None:
        return Node(x, None, None)
    else:
        if tree.x > x:
            tree.l = wstaw(x, tree.l)
        elif tree.x < x:
            tree.r = wstaw(x, tree.r)
        return tree
def wstaw2(x, tree):
    if tree.x > x:
        if tree.l:
            wstaw2(x, tree.l)
        else:
            tree.l = Node(x, None,None)
    elif tree.x < x:
        if tree.r:
            wstaw2(x, tree.r)
        else:
            tree.r = Node(x, None, None)
            
def postfix(tree):
    if tree:
        postix(tree.l)
        postix(tree.r)
        print(x)
    else:
        pass
def infix(tree):
    tab = []
    def pom(tree):
        if tree:
            pom(tree.l)
            tab.append(tree.x)
            pom(tree.r)
    pom(tree)
    return tab
# infix dziala w czasie liniowym 


def prefix(tree):
    pass

def poziomy(tree):
    tab= []
    def pom(tree, h):
        if tree:
            if h < len(tab):
                tab[h].append(tree)
            else: 
                tab.append([tree.x])
            pom(tree.l, h+1)
            pom(tree.r, h+1)
        pom(tree, 0)
        return tab

def zly_prefix(tree):
    if tree:
        return [tree.x] + zly_prefix(tree.l) + zly_prefix(tree.r)
    
# 1\1.5-2-3-4-5-6 zle drzewo
# dziala w czasie liniowym
    
    
    
    
    
    
    
    
    
    