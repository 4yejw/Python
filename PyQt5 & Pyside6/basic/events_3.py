import sys

from PySide6.QtCore import Qt
from PySide6.QtGui import QAction
from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QMenu,
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

    def context1MenuEvent(self, e):
        context1 = QMenu(self)
        context1.addAction(QAction("test 1", self))
        context1.addAction(QAction("test 2", self))
        context1.addAction(QAction("test 3", self))
        context1.exec(e.globalPos())


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
