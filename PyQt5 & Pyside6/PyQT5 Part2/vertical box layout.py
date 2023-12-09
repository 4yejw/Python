import sys
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Vertical Box Layout")
        self.setGeometry(350,150,400,400)
        self.UI()

    def UI(self):
        vbox=QVBoxLayout() #layout도 하나의 객체로 취급한다  레이아웃 : 위젯들을 담는 그릇
        button1=QPushButton("Save")
        button2=QPushButton("Exit")
        button3=QPushButton("Hello")
        vbox.addStretch() #화면이 늘어나면 버튼 크기도 같이 늘어난다
        vbox.addWidget(button1)
        vbox.addWidget(button2)
        vbox.addWidget(button3)
        vbox.addStretch()
        self.setLayout(vbox) #vbox를 윈도우의 레이아웃으로 설정한다

        self.show()


def main():
    App=QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())

if __name__=='__main__':
    main()