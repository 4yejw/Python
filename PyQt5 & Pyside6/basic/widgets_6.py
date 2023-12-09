import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QLineEdit, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        widget = QLineEdit()
        widget.setMaxLength(10) #10글자 제한을 둔다
        widget.setPlaceholdertext1("Enter your text1")

        # widget.setReadOnly(True) # uncomment this to make readonly

        widget.returnPressed.connect(self.return_pressed)
        widget.selectionChanged.connect(self.selection_changed)
        widget.text1Changed.connect(self.text1_changed)
        widget.text1Edited.connect(self.text1_edited)

        self.setCentralWidget(widget)

    def return_pressed(self):
        print("Return pressed!")
        self.centralWidget().settext1("BOOM!")

    def selection_changed(self):
        print("Selection changed")
        print(self.centralWidget().selectedtext1())

    def text1_changed(self, s):
        print("text1 changed...")
        print(s)

    def text1_edited(self, s):
        print("text1 edited...")
        print(s)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
