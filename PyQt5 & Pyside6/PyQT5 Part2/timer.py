import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QTimer

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Using Timer")
        self.setGeometry(250,150,350,350)
        self.UI()


    def UI(self):
        self.colorLabel=QLabel(self)
        self.colorLabel.resize(250,250)
        self.colorLabel.setStyleSheet("background-color:green") #original color
        self.colorLabel.move(40,20)
        ######################Buttons##################
        btnStart=QPushButton("Start",self)
        btnStart.move(80,300)
        btnStart.clicked.connect(self.start)
        btnStop=QPushButton("Stop",self)
        btnStop.move(190,300)
        btnStop.clicked.connect(self.stop)
        ##################Timer########################
        self.timer=QTimer()
        self.timer.setInterval(1000) # 1초 = 1000ms
        self.timer.timeout.connect(self.changeColor) #멈추면 timeout이벤트가 발생하지 않는다
        self.value=0

        self.show()

    def changeColor(self):
        if self.value==0:
            self.colorLabel.setStyleSheet("background-color:yellow") #yellow
            self.value=1
        else:
            self.colorLabel.setStyleSheet("background-color:red") #red
            self.value=0
    def start(self):
        self.timer.start()

    def stop(self):
        self.timer.stop()


def main():
    App = QApplication(sys.argv)
    window=Window()
    window.start()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()