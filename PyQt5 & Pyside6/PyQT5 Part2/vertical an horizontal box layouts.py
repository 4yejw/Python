import sys
from PyQt5.QtWidgets import *

#수직 수평 레이아웃

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Vertical and horizontal Box Layouts")
        self.setGeometry(350,150,400,400)
        self.UI()

    def UI(self):
        mainLayout=QVBoxLayout()
        topLayout=QHBoxLayout()
        bottomLayout=QHBoxLayout()
        mainLayout.addLayout(topLayout) #먼저 올린게 제일 위로 올라감 ^^ 순서가 중요 
        mainLayout.addLayout(bottomLayout)

        cbox=QCheckBox()
        rbtn=QRadioButton()
        combo=QComboBox()
        btn1=QPushButton()
        btn2=QPushButton()
        topLayout.setContentsMargins(150,10,20,20) #left,top,right,bottom
        topLayout.addWidget(cbox)
        topLayout.addWidget(rbtn)
        topLayout.addWidget(combo)
        bottomLayout.setContentsMargins(150,10,150,10)
        bottomLayout.addWidget(btn1)
        bottomLayout.addWidget(btn2)

        self.setLayout(mainLayout)


        self.show()


def main():
    App=QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())

if __name__=='__main__':
    main()