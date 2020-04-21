class Cell:
    def __init__(self, qc):
        self.qc = qc
    def __add__(self, other):
        print(self.qc + other.qc)
    def __sub__(self, other):
        print(self.qc - other.qc) if (self.qc - other.qc) > 0 else print('Разность меньше нуля')
    def __mul__(self, other):
        print(self.qc * other.qc)
    def __truediv__(self, other):
        print(round(self.qc // other.qc))
    def make_order(self, cells):
        row = ''
        for i in range(int(self.qc / cells)):
            row += f'{"*" * cells}\\n'
        row += f'{"*" * (self.qc % cells)}'
        print(row)

cell1 = Cell(13)
cell2 = Cell(7)
cell1 + cell2
cell1 - cell2
cell1 * cell2
cell1 / cell2
cell1.make_order(4)
cell2.make_order(3)