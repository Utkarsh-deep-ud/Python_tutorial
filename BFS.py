from collections import deque 
class Node:
    def __init__ (self,val):
        self.val = val
        self.left=None
        self.right=None
o=Node(1)
t=Node(2)
th=Node(3)
f=Node(4)
ff=Node(5)
s=Node(6)
ss=Node(7)


o.left=t
t.left=f
t.right=ff
o.right=th
th.left=s
th.right=ss

def level_order(node):
    result=[]
    q=deque([])
    q.append(node)
    while len(q)!=0:
        e=q.popleft()
        result.append(e.val)
        if e.left is not None:
            q.append(e.left)
        if e.right is not None:
            q.append(e.right)
    return result
x=level_order(o)
print("->".join(map(str,level_order(o))))
# above line very beneficialllllll




