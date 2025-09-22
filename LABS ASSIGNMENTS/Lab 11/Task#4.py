class BST:
    """Binary Search Tree with insert and inorder traversal."""
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if self.value is None:
            self.value = value
            return
        if value < self.value:
            if self.left: self.left.insert(value)
            else: self.left = BST(value)
        else:
            if self.right: self.right.insert(value)
            else: self.right = BST(value)

    def inorder(self):
        res = []
        if self.left: res.extend(self.left.inorder())
        if self.value is not None: res.append(self.value)
        if self.right: res.extend(self.right.inorder())
        return res

    def display(self):
        print("BST inorder traversal:", self.inorder())


# ---------- TESTS ----------
if __name__ == "__main__":
    bst = BST()
    for v in [50, 30, 70, 20, 40, 60, 80]:
        bst.insert(v)
    inorder = bst.inorder()
    bst.display()
    assert inorder == [20, 30, 40, 50, 60, 70, 80]
    print("✅ All BST test cases passed successfully!")
