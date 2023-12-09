import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.label = QLabel("Click in this window")
        self.setCentralWidget(self.label)

    def mouseMoveEvent(self, e):
        pos = e.pos()
        global_pos = e.globalPos() #position은 창을 기준으로, global position은 모니터 창 전체를 기준 (윈도우 기준점 좌상단 0,0)
        #position은 음수가 나올 수 있는데 global position은 음수가 나올 수없다 좌상단이 0,0이고 그 우하단으로 양의 값으로 증가하므로
        self.label.settext1("mouseMoveEvent: %s %s " % (pos, global_pos))

    # tag::mousePressEvent[]
    def mousePressEvent(self, e):
        if e.button() == Qt.LeftButton:
            # handle the left-button press in here
            self.label.settext1("mousePressEvent LEFT")

        elif e.button() == Qt.MiddleButton:
            # handle the middle-button press in here.
            self.label.settext1("mousePressEvent MIDDLE")

        elif e.button() == Qt.RightButton:
            # handle the right-button press in here.
            self.label.settext1("mousePressEvent RIGHT")

    def mouseReleaseEvent(self, e):
        if e.button() == Qt.LeftButton:
            self.label.settext1("mouseReleaseEvent LEFT")

        elif e.button() == Qt.MiddleButton:
            self.label.settext1("mouseReleaseEvent MIDDLE")

        elif e.button() == Qt.RightButton:
            self.label.settext1("mouseReleaseEvent RIGHT")

    def mouseDoubleClickEvent(self, e):
        if e.button() == Qt.LeftButton:
            self.label.settext1("mouseDoubleClickEvent LEFT")

        elif e.button() == Qt.MiddleButton:
            self.label.settext1("mouseDoubleClickEvent MIDDLE")

        elif e.button() == Qt.RightButton:
            self.label.settext1("mouseDoubleClickEvent RIGHT")

    # end::mousePressEvent[]


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
