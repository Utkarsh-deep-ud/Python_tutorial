from collections import deque
# this is not recursive approach iterative solution:
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

one.left=two
one.right=three
two.left=four
two.right=five
three.left=six
three.right=seven
six.left=eight
eight.right=nine

# now begins the actual code:

def level_order(root):  
    if root is None:
        return 0
    queue=deque([])
    height =0 
    queue.append(root)
    while len(queue)!=0:
        level_size = len(queue)
        height+=1
        for _ in range(level_size):
            e=queue.popleft()
            if e.left is not None:
                queue.append(e.left)
            if e.right is not None:
                queue.append(e.right)
    return height
print(level_order(one))
