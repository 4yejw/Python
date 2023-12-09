import sys

from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
)  # <1>


# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow): #mywindow라고 하든 뭐든
    def __init__(self):
        super().__init__()  # <2>

        self.setWindowTitle("My App")

        button = QPushButton("Press Me!")

        # Set the central widget of the Window.
        self.setCentralWidget(button)  # <3> #중앙에 버튼 위젯을 설치해라


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
