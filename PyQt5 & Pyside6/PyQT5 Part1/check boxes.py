import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Using Labels")
        self.setGeometry(150,150,500,500)
        self.UI()


    def UI(self):
        self.name=QLineEdit(self) #입력가능한 텍스트 창
        self.name.setPlaceholdertext1("이름 입력") #텍스트 창 안에 힌트를 Placeholdertext1라고 한다
        self.surname=QLineEdit(self) # "
        self.surname.setPlaceholdertext1("성 입력")# "
        self.name.move(150,50) #위치 잡기
        self.surname.move(150,80)
        self.remember=QCheckBox("Remember me",self) #Check box : Checked / Unchecked 두가지 상태
        self.remember.move(150,110)
        button=QPushButton("Submit",self) #클릭했을 때 아래 정의된 Submit을 호출하라
        button.move(200,140) #버튼 위치 이동
        button.clicked.connect(self.submit) #버튼과 submit을 연결

        self.show()

    def submit(self):
        if (self.remember.isChecked()):
            print("Name : "+self.name.text1()+ "\nSurname: "+self.surname.text1()+"\nRemember me checked")
        else:
            print("Name : "+self.name.text1()+ "\nSurname: "+self.surname.text1()+"\nRemember me not checked")
            #print는 콘솔에 출력하는 것입니다

def main():
    App = QApplication(sys.argv)
    window=Window()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()