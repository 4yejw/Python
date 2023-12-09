import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QCheckBox, QMainWindow

#^^^^^^^^^^^^^^ 신경써서 보세요 여기부터 ^^^^^^^^
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        widget = QCheckBox("This is a checkbox") #위젯은 체크박스,
        widget.setCheckState(Qt.Checked)#체크박스의 상태값을 가져온다

        # For tristate: widget.setCheckState(Qt.PartiallyChecked)
        # Or: widget.setTristate(True)
        widget.stateChanged.connect(self.show_state) #상태 변화한다면 그 상태를 보여줘라

        self.setCentralWidget(widget)

    def show_state(self, s):
        print(s == Qt.Checked) #check state 인 True or False 가 출력된다
        print(s)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
