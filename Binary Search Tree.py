class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def insert(root,value):
    if root is None:
        return Node(value)

    if value<root.data:
        root.left=insert(root.left,value)
    elif value>root.data:
        root.right=insert(root.right,value)
    return root

root=None
numbers=[50,30,70,20,40,60,80]
for i in numbers:
    root=insert(root,i)
'''
to check the elements
print(root.data)
print(root.left.data)
print(root.right.data)
print(root.left.left.data)
print(root.left.right.data)
print(root.right.left.data)
print(root.right.right.data)
'''
def Search(root,value):
    if root is None:
        return False
    if root.data==value:
        return True
    if value<root.data:
        return Search(root.left,value)
    else:
        return Search(root.right,value)
target=int(input("Enter a target: "))
if Search(root,target):
    print(f"The Target {target} is there..!")
else:
    print(f"The Target {target} is not found..!")
     

