class BST:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def add(self, key):
        if key < self.key:
            if self.left is None:
                self.left = BST(key)
            else:
                self.left.add(key)
        elif key > self.key:
            if self.right is None:
                self.right = BST(key)
            else:
                self.right.add(key)
                
    # naloga 1.
    def hide_even(self):
        pass

    # naloga 2.
    def hide_right(self):
        pass

    # naloga 3.
    def sum_level(self, level):
        pass


def tree_from_list(lst):
    if not lst:
        return None
    root = BST(lst[0])
    for key in lst[1:]:
        root.add(key)
    return root
