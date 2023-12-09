import sys
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Using Labels")
        self.setGeometry(150,150,350,350)
        self.UI() #show가 없는 대신 UI를 호출했다


    def UI(self):
        text11=QLabel("Hello Python",self)
        text12=QLabel("Hello World",self)
        text11.move(50,50) #text1 label을 출력할 장소를 이동시킨다
        text12.move(200,150) #text1 label을 출력할 장소를 이동시킨다
        self.show()

#밑의 이 부분은 항상 똑같다
def main():
    App = QApplication(sys.argv)
    window=Window() #객체를 생성한다
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()