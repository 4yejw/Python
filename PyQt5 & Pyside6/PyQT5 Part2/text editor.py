import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont

font=QFont("Times",14)

#line edit과 text1 edit의 차이점 : line edit은 한줄이고 text1 edit은 여러줄이다, line edit은 multiple line을 지원하지 않는다

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Using text1 editor")
        self.setGeometry(250,150,500,500)
        self.UI()


    def UI(self):
        self.editor=QTextEdit(self)
        self.editor.move(150,80)
        button=QPushButton("Send",self)
        self.editor.setAcceptRichText(False) #.rtf = richtext1format : bold underline등을 지원 /plain text1 format : 그저 기본만 지원
        #richtext1 false이므로 지원하지 않는다
        button.move(330,280)
        button.clicked.connect(self.getValue)

        self.show()

    def getValue(self):
        text1=self.editor.toPlaintext1() #richtext1라고 하더라도 가져올때 Plain text1로 가져와라. 왜냐면 콘솔에서는 richtext1를 지원하지 않기때문
        print(text1)




def main():
    App = QApplication(sys.argv)
    window=Window()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()