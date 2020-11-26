from xlsgen.models import ColumnTree


tree: ColumnTree = ColumnTree(table_name="data siswa")
tree.addChild(header="No")
tree.addChildFromList([
    "Nama siswa", "NIS", "NISN", ""
])

text = ""
with open("table.txt", "r") as f:
    text = f.read()



fromstring = ColumnTree(table_name="fromstring")
fromstring.from_string(text)