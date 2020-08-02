class Node:

    def __init__(self, value = None):
        self.color = 0
        self.value = value
        self.left = None
        self.right = None

class BSTree:

    def __init__(self):
        self.root = None

    def __Insert(root, value):
        
        if root == None:
            new_node = Node(value)
            return new_node
        
        elif root.value > value:
            root.left = BSTree.__Insert(root.left, value)

        else:
            root.right = BSTree.__Insert(root.right, value)

        return root

    def __Find(root, value):

        if root == None:
            return None

        elif root.value == value:
            return root
        
        elif root.value > value:
            return BSTree.__Find(root.left, value)

        else:
            return BSTree.__Find(root.right, value)

    def __Height(root):
        
        if root == None:
            return -1
        
        L = BSTree.__Height(root.left)
        R = BSTree.__Height(root.right)

        if L < R:
            return 1 + R
        else:
            return 1 + L
    
    def __Maximum(root):

        if root == None:
            return None
        
        if root.right == None:
            return root

        else:
            return BSTree.__Maximum(root.right)

    def __Minimun(root):
        
        if root == None:
            return None
        
        if root.left == None:
            return root
        else:
            return BSTree.__Minimun(root.left)

    def __Predecessor(root):
        
        if root == None:
            return None

        return BSTree.__Maximum(root.left)

    def __Successor(root):
        
        if root == None:
            return None
        
        return BSTree.__Minimun(root.right)

    def __Delete(root, value):

        if root == None:
            return None

        if root.value == value:

            #case 01:
            if root.left == None and root.right == None:
                return None
            #case 02: 
            #left child is not empty
            if root.left != None and root.right == None:
                return root.left
            #right child is not emplty
            if root.left == None and root.right != None:
                return root.right
                
            if root.left != None:
                pre = BSTree.__Predecessor(root)
                root.value = pre.value
                root.left = BSTree.__Delete(root.left, pre.value)

            else:
                succ = BSTree.__Successor(root)
                root.value = succ.value
                root.right = BSTree.__Delete(root.right, succ.value)

            return root
        
        if root.value > value:
            root.left = BSTree.__Delete(root.left, value)
        else:
            root.right = BSTree.__Delete(root.right, value)

        return root
 

    def __FindIsLeft(root, value):
        
        if root == None:
            return None
        
        if root.left !=None:
            if root.left.value == value:
                return True
        
        if root.value > value:
            return BSTree.__FindIsLeft(root.left, value)

        if root.value < value:
            return BSTree.__FindIsLeft(root.right, value)
        
        return False

    def __FindIsRight(root, value):
        
        if root == None:
            return None
        
        if root.right !=None:
            if root.right.value == value:
                return True
        
        if root.value > value:
            return BSTree.__FindIsRight(root.left, value)

        if root.value < value:
            return BSTree.__FindIsRight(root.right, value)
        
        return False
        
    def __GetSibling(root, value):
        
        if root == None:
            return None
        
        if root.right !=None and root.left != None:
            if root.right.value == value:
                return root.left
            
            if root.left.value == value:
                return root.right
        
        if root.right != None and root.left == None:
            if root.right == value:
                return None

        if root.left != None and root.right == None:
            if root.left == value:
                return None

        if root.value > value:
            return BSTree.__GetSibling(root.left, value)

        if root.value < value:
            return BSTree.__GetSibling(root.right, value)
    
    
    def __GetUncle(root, value):
        
        if root == None:
            return None
        
        if root.left != None:
            if root.left.left != None:
                if root.left.left.value == value:
                    if root.right != None:
                        return root.right
                    else:
                        return None

        if root.left != None:
            if root.left.right != None:
                if root.left.right.value == value:
                    if root.right != None:
                        return root.right
                    else:
                        return None

        if root.right != None:
            if root.right.right != None:
                if root.right.right.value == value:
                    if root.left !=None:
                        return root.left
                    else:
                        return None
        
        if root.right != None:
            if root.right.left != None:
                if root.right.left.value == value:
                    if root.left !=None:
                        return root.left
                    else:
                        return None

        if root.value > value:
            return BSTree.__GetUncle(root.left, value)

        if root.value < value:
            return BSTree.__GetUncle(root.right, value)
   

    def __RotateLeft(root, v):
        y = v.right
        v.right = y.left

        if y.left != None:
            y.left.root = v
        
        parentofy = BSTree.__Predecessor(y)
        parentofv = BSTree.__Predecessor(v)
        parentofy = parentofv

        if parentofv == None:
            root = y
        elif v == parentofv.left:
            parentofv.left = y
        else:
            parentofv.right = y
        
        y.left = v
        parentofv = y
    
    def __RotateRight(root, v):
        y = v.left
        v.left = y.right

        if y.right != None:
            y.right.root = v

        parentofy = BSTree.__Predecessor(y)
        parentofv = BSTree.__Predecessor(v)
        parentofy = parentofv

        if parentofv == None:
            root = y
        elif v == parentofv.right:
            parentofv.right = y
        else:
            parentofv = y
        
        y.right = v
        parentofv = y
            
    #Required Methods
    def Insert(self, value):
        self.root = BSTree.__Insert(self.root, value)

    def Find(self, value): 
        return BSTree.__Find(self.root, value)

    def Height(self):
        return BSTree.__Height(self.root)
        
    def Delete(self, value):

        check = self.Find(value)
        if check != None:
            self.root = BSTree.__Delete(self.root, value)
            check_01 = self.Find(value)
            if check_01 == None:
                return True
        else:
            return False
        
    def IsLeft(self, value):
        return BSTree.__FindIsLeft(self.root, value)

    def IsRight(self, value):
        return BSTree.__FindIsRight(self.root, value)
    
    def GetSibling(self, value): 
        return BSTree.__GetSibling(self.root, value)

    def GetUncle(self, v):
        return BSTree.__GetUncle(self.root, v)

    def RotateLeft(self, v):
        node = self.Find(v)
        if node!=None:
            BSTree.__RotateLeft(self.root, node)

    def RotateRight(self, value):
        node = self.Find(value)
        if node!= None:
            BSTree.__RotateRight(self, node)

    def Build(self, data: list):
        for i in data:
            self.Insert(i)


def Test_BSTree():
    t = BSTree()
    t.Build([5,6,3,1,2,4])

#Drive code
Test_BSTree()


