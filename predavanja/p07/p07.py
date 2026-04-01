class BST:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def insert(self, key):
        if key < self.key:
            if self.left:
                self.left.insert(key)
            else:
                self.left = BST(key)
        elif key > self.key:
            if self.right:
                self.right.insert(key)
            else:
                self.right = BST(key)
        return self

    def search(self, key):
        if self.key == key:
            return self
        elif key < self.key and self.left:
            return self.left.search(key)
        elif key > self.key and self.right:
            return self.right.search(key)
        else:
            return None

    def delete(self, key):
        if key < self.key:
            if self.left:
                self.left = self.left.delete(key)
            return self
        elif key > self.key:
            if self.right:
                self.right = self.right.delete(key)
            return self
        else:  
            if self.left is None:
                return self.right  # Poveži starša z desnim otrokom
            elif self.right is None:
                return self.left  # Poveži starša z levim otrokom

            # Vozlišče ima dva otroka: poišči (najmanjši v desnem poddrevesu)
            min_key = self.right.find_min()
            self.key = min_key  
            self.right = self.right.delete(min_key)  
            return self

    def find_min(self):
        if self.left == None:
            return self.key
        return self.left.find_min()
    
    def height(self):
        left_h = 0 if not self.left else 1+self.left.height()
        right_h = 0 if not self.right else 1+self.right.height()
        return max(left_h, right_h)
    
    def inorder(self):
        if self.left:
            self.left.inorder()
        print(self.key)
        if self.right:
            self.right.inorder()

def getHeight(t):
    if t == None:
        return 0
    return 1+t._height

class AVL:
    def __init__(self, key):
 
        self.key = key
        self.left = None
        self.right = None
        self._height = 0

    def correct_height(self):
        self._height = max(getHeight(self.left), getHeight(self.right))

    def rotateL(self):
        t2 = self.right.left
        self.right.left = self
        new_root = self.right
        self.right = t2
        # višine
        self.correct_height()
        new_root.correct_height()

        return new_root
    
    def rotateR(self):
        t2 = self.left.right
        self.left.right = self
        new_root = self.left
        self.left = t2
        # višine
        self.correct_height()
        new_root.correct_height()

        return new_root

    def balance(self):
        return getHeight(self.left) - getHeight(self.right)  

    def insert(self, key):
        if key < self.key:
            if self.left:
                self.left = self.left.insert(key)  
            else:
                self.left = AVL(key)
            if self.balance()>1:
                if self.left.balance()>0:
                    return self.rotateR()
                else: # 
                    self.left = self.left.rotateL()
                    return self.rotateR()
        elif key > self.key:
            if self.right:
                self.right = self.right.insert(key)  
            else:
                self.right = AVL(key)
            if self.balance()<-1:
                if self.right.balance()<0:
                    return self.rotateL()
                else: # 
                    self.right = self.right.rotateR()
                    return self.rotateL()

        l_height = getHeight(self.left)
        r_height = getHeight(self.right)
        self._height = max(l_height, r_height)
        return self
    
    def num_nodes(self):
        left_n = self.left.num_nodes() if self.left else 0
        right_n = self.right.num_nodes() if self.right else 0
        return 1+left_n+right_n

    def search(self, key):
        if self.key == key:
            return self
        elif key < self.key and self.left:
            return self.left.search(key)
        elif key > self.key and self.right:
            return self.right.search(key)
        else:
            return None
    
    def sum(self):
        lSum = self.left.sum() if self.left else 0
        rSum = self.right.sum() if self.right else 0
        return self.key + lSum + rSum

    def printT(self):
        print(self.key)
        if self.left:
            self.left.printT()
        if self.right:
            self.right.printT()
    
    def height(self):
        left_h = 0 if not self.left else 1+self.left.height()
        right_h = 0 if not self.right else 1+self.right.height()
        return max(left_h, right_h)

# Experiment
import random
t = None
for i in range(1000000):
    data = random.randint(1, 10000000)
    if t is None:
        t = AVL(i)
    else:
        t=t.insert(i)

print(t.height())