import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont

font = QFont("Times", 16)

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Using Spin Boxes")
        self.setGeometry(250, 150, 500, 500)
        self.UI()

    def UI(self):
        self.text1 = QLabel("hello", self)  # Use self.text1 as an instance variable
        #self.text1.resize()
        self.text1.move(300, 3000)

        self.spinBox = QSpinBox(self)
        self.spinBox.move(150, 100)
        self.spinBox.setFont(font)
        self.spinBox.setRange(0, 110)
        self.spinBox.setPrefix("$ ")
        self.spinBox.setSingleStep(10)
        self.spinBox.valueChanged.connect(self.getValue)
        self.show()

    def getValue(self):
        value = self.spinBox.value()
        print("${} -> {}원".format(value, 1300 * int(value)))
       # self.text1.settext1("{} -> {}원".format(value, 1300 * int(value)))  # Use self.text1 to set the text1

def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()
