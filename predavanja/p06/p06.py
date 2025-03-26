class TreeNode:
    def __init__(self, data, children):
        self.data = data
        self.children = children #seznam otrok


# Filesystem

class FSNode:
    def __init__(self, name, is_dir=False, children=None):
        self.name = name
        self.is_dir = is_dir
        self.children = children if is_dir else []
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
        
        mHeight = 0
        for c in self.children:
            h = c.height()
            if h>mHeight:
                mHeight = h
        return 1+mHeight
        
    
    def count_nodes(self):
        if self.children == []:
            return 1
        nSum = 0
        for c in self.children:
            nSum +=c.count_nodes()
        return 1+nSum
    
    def count_leaves(self):
        if self.children == []:
            return 1
        nSum = 0
        for c in self.children:
            nSum +=c.count_leaves()
        return nSum

    def size_in_bytes():
        pass
    
    # obhodi
    def pre_order(self):
        print(self.name)
        for c in self.children:
            c.pre_order()

    def post_order(self):
        for c in self.children:
            c.post_order()
        print(self.name)


def make_dummy_fs():
    f1 =FSNode("slikca.png")
    f2 =FSNode("program.py")
    f3 =FSNode("seminar.docx")
    f4 =FSNode("film.mpeg")
    d1 = FSNode("Filmi", True, [f4])
    d2 = FSNode("Faks", True, [f2,f3])
    d5 = FSNode("Slike", True, [f1])
    d3 = FSNode("Dokumenti", True, [d5])
    d4 = FSNode("Namizje", True, [d1,d2,d3])
    return d4
    