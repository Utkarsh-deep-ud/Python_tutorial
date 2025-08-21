class Node:
    def __init__ (self,val):
        self.val=val
        self.left=None
        self.right=None

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

# This is wrong approach as we are trying to directly assigning int val to node which is wrong.
# five.left = 3 
# three.left = 2
# three.right = 9
# five.right = 4 
# four.left = 8
# eight.left = 1
# eight.right = 6
# four.right = 10

five.left = three
three.left = two
three.right = nine
five.right = four 
four.left = eight
eight.left = one
eight.right = six
four.right = ten


def preorder(node):
    if node==None:
        return
    print(node.val,"->",end="")
    preorder(node.left)
    preorder(node.right)
preorder(five)