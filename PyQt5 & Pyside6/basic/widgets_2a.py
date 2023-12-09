import sys

from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__() #여기까지는 똑같다

        self.setWindowTitle("My App")

        widget = QLabel("Hello") #아까는 text1였지만 여기에서는 widget으로 사용하고있다
        widget.setPixmap(QPixmap("otje.jpg"))

        self.setCentralWidget(widget)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
