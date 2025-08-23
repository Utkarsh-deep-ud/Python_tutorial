class Node:
    def __init__ (self,val):
        self.val = val
        self.left= None
        self.right=None
# Create nodes
a = Node(3)
b = Node(3)
c = Node(1)
d = Node(2)
e = Node(1)
f = Node(3)
g = Node(1)
h = Node(1)
i = Node(6)
j = Node(8)
k = Node(2)
l = Node(6)
m = Node(9)
n=Node(10)
o=Node(5)

a.left = b
b.left=c
b.right=d
a.right=e
e.left=f
f.left=g
g.left=h
g.right=k
h.left=i
i.right=j
e.right=l
l.right=m
m.right=n
n.left=o

# Now the actual code begins:

diameter=0
def solve(node):
    global diameter
    if node==None:
        return 0
    leftheight=solve(node.left)
    rightheight=solve(node.right)
    diameter = max(diameter,leftheight+rightheight)
    return 1+max(leftheight,rightheight)
solve(a)
print(diameter)



