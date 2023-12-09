import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QComboBox, QMainWindow

#콤보박스에서의 이벤트 발생 경우
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        widget = QComboBox()
        widget.addItems(["One", "Two", "Three"])

        widget.currentIndexChanged.connect(self.index_changed) #인덱스가 바뀌었을때 인덱스_changed를 실행
        widget.currenttext1Changed.connect(self.text1_changed) #텍스트가 변화하는 이벤트가발생했을때 뒤의 메소드를 실행

        self.setCentralWidget(widget)

    def index_changed(self, i):  # i is an int
        print(i)

    def text1_changed(self, s):  # s is a str
        print(s)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
