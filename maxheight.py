# this approach is recurrsive approach

class Node:
    def __init__ (self,val):
        self.val= val
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

one.left=two
one.right=three
two.left=four
two.right=five
three.left=six
three.right=seven
six.left=eight
eight.right=nine

# now begins the actual code:

def solve(node):
    if node==None:
        return 0
    leftheight = solve(node.left)
    rightheight = solve(node.right)

    return 1+max(leftheight,rightheight)

print(solve(one))