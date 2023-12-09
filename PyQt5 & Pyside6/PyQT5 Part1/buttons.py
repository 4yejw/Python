import sys
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Using Labels")
        self.setGeometry(150,150,350,350)
        self.UI() #여기까지 앞은 똑같다

    #윈도우는 이벤트 드리블 프로그램이다 , 이벤트가 발생하지 않으면 아무일도 하지 않는다

    def UI(self):
        self.text1=QLabel("아래 버튼을 누르세요",self) #레이블을 만든다
        startButon= QPushButton("Enter",self) #Enter라는 버튼 객체를 생성한다
        exitButon= QPushButton("Exit",self) #exit라는 버튼 객체를 생성한다
        self.text1.move(100,50) #"아래 버튼을 누르세요" 위치 조정
        startButon.move(100,80)#엔터 버튼 위치 이동
        exitButon.move(200,80) #exit버튼 위치 이동
        startButon.clicked.connect(self.startFunc) #저 함수를 동작시켜라 ^^
        exitButon.clicked.connect(self.exitFunc) #이 버튼 클릭 이벤트가 발생했을 때 해야할 일들을 함수나 메소드로 정의해준다 ^^
        self.show()

    def startFunc(self): #버튼을 클릭했을 때 동작할 함수/메소드
        self.text1.settext1("You clicked Enter") #버튼을 클릭했을 때 text1의 내용을 바꾼다
        self.text1.resize(150,20) #텍스트 크기 조절
        self.text1.move(160,300) #텍스트 위치 조절
    def exitFunc(self):
        self.text1.settext1("You clicked Exit") #버튼을 눌렀을 때 text1를 출력한다
        self.text1.resize(150,20) #텍스트 위치 조절

#아래는 이전과 같다 
def main():
    App = QApplication(sys.argv)
    window=Window()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()