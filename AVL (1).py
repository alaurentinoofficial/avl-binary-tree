
# coding: utf-8

# In[1]:


class BinaryTree():
    def __init__(self, key=0, value=None, top=None):
        self.top = None
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self._lenght = 0 if value == None else 1
        self._count = 0
    
    def __bool__(self):
        return self._lenght > 0
    
    def __str__(self):
        result = ""
        
        for item in BinaryTree.order(self):
            result += ", " + str(item)
        
        return "[" + result[2:] + "]"
    
    def __repr__(self):
        result = ""
        
        for item in BinaryTree.pre_order(self):
            result += ", " + str(item)
        
        return "BinaryTree([" + result[2:] + "])"
    
    def __getitem__(self, key):
        return self.search(key).value
    
    def __setitem__(self, key, value):
        item = self.search(key)
        item.value = value
    
    def __delitem__(self, key):
        BinaryTree.remove(self, key)
    
    def __contains__(self, key):
        try:
            self.search(key)
            return True
        except ValueError:
            return False
    
    def __iter__(self):
        self._values = []
        
        for item in BinaryTree.pre_order(self):
            self._values.append(item)
            
        return self
    
    def __next__(self):
        if len(self._values) > 0:
            value = self._values[0]
            self._values.pop(0)
            return value
        else:
            raise StopIteration()
    
    def __lt__(self, item):
        if isinstance(item, BinaryTree):
            return self.key < item.key
        elif type(item) == int:
            return self.key < item
        else:
            raise ValueError("Invalid type comparation!")
    
    def __le__(self, item):
        if isinstance(item, BinaryTree):
            return self.key <= item.key
        elif type(item) == int:
            return self.key <= item
        else:
            raise ValueError("Invalid type comparation!")
    
    def __gt__(self, item):
        if isinstance(item, BinaryTree):
            return self.key > item.key
        elif type(item) == int:
            return self.key > item
        else:
            raise ValueError("Invalid type comparation!")
    
    def __ge__(self, item):
        if isinstance(item, BinaryTree):
            return self.key >= item.key
        elif type(item) == int:
            return self.key >= item
        else:
            raise ValueError("Invalid type comparation!")
    
    def __eq__(self, item):
        if isinstance(item, BinaryTree):
            return self.key == item.key
        else:
            return self.key == item
    
    def __ne__(self, item):
        if isinstance(item, BinaryTree):
            return self.key != item.key
        else:
            return self.key != item
    
    def append(self, value, key=None):
        key = self.lenght if key == None else key
        
        BinaryTree.add(self, BinaryTree(key, value))
            
    def search(self, key):
        actual = self
        
        while(actual != None):
            
            if key < actual.key:
                actual = actual.left
            elif key > actual.key:
                actual = actual.right
            else:
                return actual
    
        raise ValueError("Index out exception!")
    
    def has_subtree(self):
        return self.right != None or self.left != None
    
    @staticmethod
    def order(tree):
        if tree != None:
            if tree.left != None:
                yield from BinaryTree.order(tree.left)
            
            yield tree.value
            
            if tree.right != None:
                yield from BinaryTree.order(tree.right)

    @staticmethod
    def pre_order(tree):
        if tree != None:
            yield tree.value
            
            if tree.left != None:
                yield from BinaryTree.pre_order(tree.left)
            
            if tree.right != None:
                yield from BinaryTree.pre_order(tree.right)
            

    @property
    def lenght(self):
        return self._lenght
    
    @staticmethod
    def add(actual, subtree): 
        actual._lenght += 1
        
        # CASE IT'S THE ROOT
        if actual.top == None and actual._lenght == 1:
            actual.key = subtree.key
            actual.value = subtree.value
        
        # NOT IS THE ROOT
        else:
            # TEST RIGHT
            if subtree.key > actual.key:

                if actual.right != None:
                    BinaryTree.add(actual.right, subtree)
                else:
                    subtree.top = actual
                    actual.right = subtree

            # TEST LEFT
            elif subtree.key < actual.key:

                if actual.left != None:
                    BinaryTree.add(actual.left, subtree)
                else:
                    subtree.top = actual
                    actual.left = subtree

            # SAME NODE
            else:
                actual.value = subtree.value
    
    @staticmethod
    def minimum(tree):
        if tree.left != None:
            return BinaryTree.minimum(tree.left)
        
        return tree
    
    @staticmethod
    def maximum(tree):
        if tree.right != None:
            return BinaryTree.maximum(tree.right)
        
        return tree
    
    @staticmethod
    def successor(tree):
        if tree.right != None:
            return BinaryTree.minimum(tree.right)
        
        top = tree.top
        
        while(top != None and tree == top.right):
            tree = top
            top = tree.top
        
        return top
    
    @staticmethod
    def predecessor(tree):
        if tree.left != None:
            return BinaryTree.maximum(tree.left)
        
        top = tree.top
        
        while(top != None and tree == top.left):
            tree = top
            top = tree.top
        
        return top
    
    @staticmethod
    def remove(tree, key):
        tree._lenght -= 1
        
        tree = tree.search(key)
        top = tree.top
        son = None
        
        # RIGHT CHILD
        if tree.right != None and tree.left == None:
            son = tree.right
            tree.right.top = top
                
        # LEFT CHILD
        elif tree.left != None and tree.right == None:
            son = tree.left
            tree.left.top = top
        
        # BOTH CHILDS
        elif tree.left != None and tree.right != None:
            successor = BinaryTree.successor(tree)
            
            # MARGE THE LEFT OF THE NODE THAT WILL BE REMOVED
            successor.left = tree.left
            tree.left.top = successor
            
            son = tree.right
            tree.right.top = top
        
        if top.right == tree:
            top.right = son
        else:
            top.left = son


# In[2]:


tree = BinaryTree()

tree.append(key=8, value=80)
tree.append(key=4, value=40)
tree.append(key=2, value=20)
tree.append(key=6, value=60)
tree.append(key=5, value=50)
tree.append(key=7, value=70)
tree.append(key=10, value=100)
tree.append(key=9, value=90)

del tree[4]

print("Lenght:\t", tree.lenght)
print("str:\t", str(tree))
print("repr:\t", repr(tree))
print("\n7 in tree: {}\n4 in tree: {}".format(7 in tree, 4 in tree))


print()
print()


print("\nInterating:")
for item in tree:
    print(item, end=", ")
    
    
print()
print()

print("5 < 7: ", (tree.search(5) < 7))
print("5 > 7: ", (tree.search(7) > tree.search(5)))
print("2 == 2: ", (tree.search(2) == tree.search(2)))
print("2 == 9: ", (tree.search(2) == tree.search(9)))


# In[31]:


class AVL(BinaryTree):
    def __init__(self, key=0, value=None, top=None):
        super().__init__(key=key, value=value, top=top)
        self._height = -1
        self._self_balance = 1
        
    @property
    def cof_balance(self):
        return self._self_balance
        
    def append(self, value, key=None):
        key = self.lenght if key == None else key
        
        BinaryTree.add(self, AVL(key, value))
    
    @property
    def height(self):
        void = not self.has_subtree()
        
        if void:
            return 0
        else:
            return self._height
        
    def set_height(self, recurssion=True):
        if self.has_subtree():
            if recurssion:
                if self.left != None:
                    self.left.set_height()
                
                if self.right != None:
                    self.right.set_height()
            
            right_value = self.right._height if self.right != None else 0
            left_value = self.left._height if self.left != None else 0
            
            
            self._height = max(right_value, left_value) + 1
        else:
            self._height = -1
            
    def set_self_balance(self, recurssion=True):
        if self.has_subtree():
            if recurssion:
                if self.left != None:
                    self.left.set_height()
                
                if self.right != None:
                    self.right.set_height()
            
            right_value = self.right._height if self.right != None else 0
            left_value = self.left._height if self.left != None else 0
            
            
            self._self_balance = left_value - right_value + 1
        else:
            self._self_balance = 0
    
    @staticmethod
    def balance(self):
        self.set_height()
        self.set_self_balance()
        
        while abs(self._self_balance) > 1:
            # LEFT
            if self._self_balance > 1:
                if self.left != None and self.left._self_balance < 0:
                    self.left.move_left()
                    self.set_height()
                    self.set_self_balance()
                self.move_right()
            
            # RIGHT
            if self._self_balance < -1:
                if self.right != None and self.right._self_balance > 0:
                    self.right.move_right()
                    self.set_height()
                    self.set_self_balance()
                self.move_left()
            
            self.set_height()
            self.set_self_balance()
    
    def changes(self, tree):
        self.key, tree.key = (tree.key, self.key,)
        self.value, tree.value = (tree.value, self.value,)
    
    def move_right(self):
        self.changes(self.left)
        part = self.left
        
        self.left = part.left
        
        # MOVE THE PART
        part.left = part.right
        part.right = self.right
        
        if part.right != None:
            part.right.top = part
        
        self.right = part
    
    def move_left(self):
        self.changes(self.right)
        part = self.right
        
        self.right = part.right
        
        # MOVE THE PART
        part.right = part.left
        part.left = self.left
        
        if part.left != None:
            part.left.top = part
        
        self.left = part


# In[36]:


tree = AVL()

tree.append(key=8, value=80)
tree.append(key=4, value=40)
tree.append(key=2, value=20)
tree.append(key=6, value=60)
tree.append(key=5, value=50)
tree.append(key=7, value=70)
tree.append(key=10, value=100)
tree.append(key=9, value=90)

del tree[4]

print("Lenght:\t", tree.lenght)
print("str:\t", str(tree))
print("repr:\t", repr(tree))
print("\n7 in tree: {}\n4 in tree: {}".format(7 in tree, 4 in tree))


print()
print()


print("\nInterating:")
for item in tree:
    print(item, end=", ")
    
    
print()
print()

print("5 < 7: ", (tree.search(5) < 7))
print("5 > 7: ", (tree.search(7) > tree.search(5)))
print("2 == 2: ", (tree.search(2) == tree.search(2)))
print("2 == 9: ", (tree.search(2) == tree.search(9)))




AVL.balance(tree)

print("\n\n>>>>>>>>> After balance <<<<<<<<<<")

print("Height:\t", tree.height)
print("Lenght:\t", tree.lenght)
print("str:\t", str(tree))
print("repr:\t", repr(tree))

print()
print()


print("\nInterating:")
for item in tree:
    print(item, end=", ")
    
    
print()
print()

print("5 < 7: ", (tree.search(5) < 7))
print("5 > 7: ", (tree.search(7) > tree.search(5)))
print("2 == 2: ", (tree.search(2) == tree.search(2)))
print("2 == 9: ", (tree.search(2) == tree.search(9)))


# In[37]:


tree.value


# In[49]:


class HashTable():
    def __init__(self):
        self._distribuition = []
    
    @staticmethod
    def fn(key):
        return hash(key) & 100000
    
    def __getitem__(self, key):
        key = HashTable.fn(key)
        return self._distribuition[key]
    
    def __setitem__(self, key, value):
        key = HashTable.fn(key)
        
        while len(self._distribuition) <= key:
            self._distribuition.append(None)
        
        self._distribuition[key] = value


# In[51]:


table = HashTable()

table["a"] = 1789
table["anderson"] = "teste"

print(table["a"])
print(table["anderson"])

