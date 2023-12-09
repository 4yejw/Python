import sys

from PySide6.QtWidgets import QApplication, QListWidget, QMainWindow

#리스트 위젯에서 이벤트 발생 경우
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        widget = QListWidget()
        widget.addItems(["One", "Two", "Three"])
        #list에서는 value를 중심으로 하기 때문에 item을 사용, 콤보박스에서는 index중심으로 하기 때문에 index사용
        widget.currentItemChanged.connect(self.index_changed) #콤보에서는 index 리스트에서는 item Changed
        widget.currenttext1Changed.connect(self.text1_changed)

        self.setCentralWidget(widget)

    def index_changed(self, i):  # Not an index, i is a QListItem ##NOT A INDEX JUST ITEM
        print(i.text1())

    def text1_changed(self, s):  # s is a str
        print(s)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
