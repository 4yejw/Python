import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap #이미지를 담기위해서 QtGui에서 QPixmap을 불러와준다


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Using Labels")
        self.setGeometry(150,150,800,600)
        self.UI()


    def UI(self):
        self.image =QLabel(self)#레이블이 이미지 역할을 한다 우리의 출력은 이미지로보이긴하지만 레이블이다.
        self.image.setPixmap(QPixmap('python.png')) #이미지를 생성
        self.image.move(150,50)
        removeButton=QPushButton("Remove",self)
        removeButton.move(150,220)
        removeButton.clicked.connect(self.removeImg)
        showButton=QPushButton("Show",self)
        showButton.clicked.connect(self.showImg)
        showButton.move(260,220)
        self.show()

    def removeImg(self):
        self.image.close()
    def showImg(self):
        self.image.show()

def main():
    App = QApplication(sys.argv)
    window=Window()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()