class Branch:
    def __init__(self, header: str, parent):
        self.is_root = False
        self.parent = parent
        self.children = []
        self.header = header

    def addChild(self, header: str = "coloumn"):
        child = Branch(header=header, parent=self)
        self.children.append(child)

    def addChildFromList(self, headers: list):
        for header in headers:
            self.addChild(header=header)

    @property
    def root(self):
        if self.parent.is_root:
            return self.parent
        else:
            return self.parent.root

    def findChild(self, header: str):
        for node in self.children:
            if node.header == header:
                return node
            res = node.findChild(header)
            if res is not None:
                return res

    def __str__(self):
        return f"<Branch {self.header}>"

    def __repr__(self):
        return f"Branch(header='{self.header}')>"

    @property
    def width_span(self):
        if len(self.children) == 0:
            return 1
        else:
            width = 0
            for node in self.children:
                width += node.width_span
            return width


class ColumnTree(Branch):

    def __init__(self, table_name: str):
        self.is_root = True
        self.children = []
        self.table_name = table_name

    def __str__(self):
        return f"<ColumnTree {self.table_name}>"

    def __repr__(self):
        return f"ColumnTree(table_name='{self.table_name}')>"

    def from_string(self, tablestring:str):
        current_parent = self
        current_level = 0
        for line in tablestring.splitlines():
            _ws = count_ws(line)
            if _ws > current_level:
                current_level = _ws
                current_parent = current_parent.children[-1]
                
            elif _ws < current_level:
                current_level = _ws
                current_parent = current_parent.parent
            
            current_parent.addChild(line.lstrip())
            print(current_parent.children)
            # TODO: detect leading spaces
        # print(tablestring)

def count_ws(string:str)-> int:
    count= 0
    for char in string:
        if char == " ":
            count += 1
        elif char == "\t":
            count += 4
        else:
            return count
            