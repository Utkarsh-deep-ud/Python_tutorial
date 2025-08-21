class Node:
    def __init__ (self,val):
        self.val = val
        self.left = None
        self.right = None
one=Node(1)
two=Node(2)
three=Node(3)
four=Node(4)
five=Node(5)
six=Node(6)
seven=Node(7)
eight=Node(8)
nine=Node(9)
ten=Node(10)

five.left = three
three.left = two
three.right = nine
five.right = four 
four.left = eight
eight.left = one
eight.right = six
four.right = ten

def postorder(node):
    if node==None:
        return
    postorder(node.left)
    postorder(node.right)
    print(node.val,"->",end="")
postorder(five)