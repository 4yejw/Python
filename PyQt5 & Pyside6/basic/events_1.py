import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    Qtext1Edit,
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.label = QLabel("Click in this window")
        self.setCentralWidget(self.label)

    def mouseMoveEvent(self, e):
        self.label.settext1("mouseMoveEvent")

    def mousePressEvent(self, e):
        self.label.settext1("mousePressEvent")

    def mouseReleaseEvent(self, e):
        self.label.settext1("mouseReleaseEvent")

    def mouseDoubleClickEvent(self, e):
        self.label.settext1("mouseDoubleClickEvent")


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
