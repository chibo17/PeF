class TreeNode:
    def __init__(self, data, children):
        self.data = data
        self.children = children #seznam otrok


# Filesystem

class FSNode:
    def __init__(self, name, is_dir=False, children=None, size=0):
        self.name = name
        self.is_dir = is_dir
        self.children = children if is_dir else []
        self.size = 10 if not is_dir and size==0 else size
        if is_dir and children is None:
            self.children = []



    def __str__(self, indent=""):
        s = indent + self.name
        if self.is_dir:
            s += "/"
            for child in self.children:
                s += "\n" + child.__str__(indent + "  ")
        return s

    
    def height(self):
        if self.children == []:
            return 0
        heights = [x.height() for x in self.children]
        return 1+max(heights)
        
    
    def count_nodes(self):
        if self.children == []:
            return 1
        counts = [x.count_nodes() for x in self.children]
        return 1+sum(counts)
    
    def count_leaves(self):
        if self.children == []:
            return 1
        counts = [x.count_leaves() for x in self.children]
        return sum(counts)

    def count_files(self):
        if not self.is_dir:
            return 1
        counts = [x.count_files() for x in self.children]
        return sum(counts)

    def size_in_bytes(self):
        if self.children == []:
            return self.size
        sizes = [x.size_in_bytes() for x in self.children]
        return sum(sizes)+self.size
    
    def obhodi(self, depth=0):
        if self.children == []:
            print(depth*"  "+self.name)
            return
        print(depth*"  "+self.name)
        for t in self.children:
            t.obhodi(depth+1)


    # obhodi
    def pre_order(self):
        pass

    def post_order(self):
        if self.children == []:
            print(self.name)
            return
        for t in self.children:
            t.post_order()
        print(self.name)


def make_dummy_fs():
    f1 =FSNode("slikca.png",size=12000)
    f2 =FSNode("program.py", size=5000)
    f3 =FSNode("seminar.docx", size=500000)
    f4 =FSNode("film.mpeg", size=100000000)
    d1 = FSNode("Filmi", True, [f4])
    d2 = FSNode("Faks", True, [f2,f3])
    d5 = FSNode("Slike", True, [f1])
    d3 = FSNode("Dokumenti", True, [d5])
    d4 = FSNode("Namizje", True, [d1,d2,d3])
    return d4
    

class ExpressionTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
    def __str__(self):
        if self.left and self.right:
            return f"({str(self.left)} {self.value} {str(self.right)})"
        else:
            return str(self.value)
    
    def evaluate(self):
        pass

def make_tree(expr):
    pass