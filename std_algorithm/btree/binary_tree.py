class BTree():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def add(tree, data):
    # if no data
    if tree == None:
        tree = BTree(data)
        return
    
    # add to the left
    if data < tree.data:
        if tree.left == None:
            tree.left = BTree(data)
        else:
            add(tree.left, data)
    # add to the right
    else:
        if tree.right == None:
            tree.right = BTree(data)
        else:
            add(tree.right, data)

def largest(tree):
    # 1. no child = root is largest
    if tree.right == None:
        largest(tree.left)
    
    cur = tree
    while cur.right != None:
        cur = cur.right

    return cur.data

def largest_2nd(tree):
    # 1. no child = root is largest
    if tree.right == None:
        largest(tree.left)

    cur = tree
    cur_pa = tree
    # get largest(cur)
    while cur.right != None:
        cur_pa = cur
        cur = cur.right
    
    # if largest has a left child
    if cur.left != None:
        largest(cur.left)
    else:
        return cur_pa.data

# it doesn't work yet
def remove(root, data):
    if root == None:
        return False
    
    if data == root.data:
        # 1. no child
        if root.left == None and root.right == None:
            root = None
        # 2-1. one child on left
        elif root.left != None and root.right == None:
            root = root.left
        # 2-2. one child on right
        elif root.left == None and root.right != None:
            root = root.right
        # 3. two child
        else:
            # 3.0 explore left side
            cur = root.right
            cur_pa = root.right
            while cur.left != None:
                cur_pa = cur
                cur = cur.left
            
            # 3.1 replace data from cur to root
            root.data = cur.data
            
            #3.2 root.right has no child
            if cur == cur_pa:
                root.right = None
            #3.3 if right has a child
            elif cur.right != None:
                cur_pa.left = cur.right
            else:
                cur_pa.left = None
            cur = None
        return
    elif data < root.data:
        remove(root.left, data)
    else:
        remove(root.right, data)
            

def findHeight(root):
    if root == None:
        return -1
    left_height = findHeight(root.left)
    right_height = findHeight(root.right)
    return max(left_height, right_height) + 1

def display(tree):
    if tree is None:
        return
    display(tree.left)
    print(tree.data, end=' ')
    display(tree.right)

"""
bt = BTree(25)
add(bt, 10)
add(bt, 13)
add(bt, 23)
add(bt, 14)
add(bt, 4)
add(bt, 42)
display(bt)
print("\nlargest:" + str(largest(bt)))
print("\nlargest 2nd:" + str(largest_2nd(bt)))
remove(bt, 23)
display(bt)

print("\nheight:" + str(findHeight(bt)))
"""

#**********************************
def bstDistance(values, n, node1, node2):
    bt = BTree(values[0])
    for i in range(len(values)):
        if i == 0: continue
        print(values[i])
        add(bt, values[i])
    
values = [5,6,3,1,2,4]
bstDistance(values, 6, 2, 4)



