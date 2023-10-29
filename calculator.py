
from  PyQt5.QtWidgets import *



app = QApplication([])



class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator")

        big_vl = QVBoxLayout()
        top_xl = QHBoxLayout()
        self.input = QLineEdit()
        self.clear_btn = QPushButton("C")
        top_xl.addWidget(self.input)
        top_xl.addWidget(self.clear_btn)
        top_w = QWidget()
        top_w.setLayout(top_xl)  # <--------- Top o f the calculator widget

        bottom_grid = QGridLayout()
        self.first = QPushButton("1")
        self.second = QPushButton("2")
        self.third = QPushButton("3")
        self.four = QPushButton("4")
        self.five = QPushButton("5")
        self.six = QPushButton("6")
        self.seven = QPushButton("7")
        self.eight = QPushButton("8")
        self.nine = QPushButton("9")
        self.zero = QPushButton("0")
        self.kopaytirish = QPushButton("*")
        self.bolish = QPushButton("/")
        self.qoshish = QPushButton("+")
        self.ayirish = QPushButton("-")
        self.tenglik = QPushButton("=")
        self.daraja = QPushButton("^2")


        bottom_grid.addWidget(self.seven,0,0)
        bottom_grid.addWidget(self.eight,0,1)
        bottom_grid.addWidget(self.nine,0,2)
        bottom_grid.addWidget(self.kopaytirish,0,3)
        bottom_grid.addWidget(self.four,1,0)
        bottom_grid.addWidget(self.five,1,1)
        bottom_grid.addWidget(self.six,1,2)
        bottom_grid.addWidget(self.ayirish,1,3)
        bottom_grid.addWidget(self.first,2,0)
        bottom_grid.addWidget(self.second,2,1)
        bottom_grid.addWidget(self.third,2,2)
        bottom_grid.addWidget(self.qoshish,2,3)
        bottom_grid.addWidget(self.daraja,3,0)
        bottom_grid.addWidget(self.zero,3,1)
        bottom_grid.addWidget(self.bolish,3,2)
        bottom_grid.addWidget(self.tenglik,3,3)



        grid_w= QWidget()
        grid_w.setLayout(bottom_grid)
        big_vl.addWidget(top_w)
        big_vl.addWidget(grid_w)
        big_w = QWidget()
        big_w.setLayout(big_vl)
        self.setCentralWidget(big_w)

        self.second.clicked.connect(self.bosildi)
        self.qoshish.clicked.connect(self.bosildi1)




a = Window()
a.show()

app.exec()
