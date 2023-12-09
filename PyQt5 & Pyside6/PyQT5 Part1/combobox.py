import sys
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Using Comboboxes")
        self.setGeometry(250,150,500,500)
        self.UI()


    def UI(self):
        self.combo=QComboBox(self)
        self.combo.move(150,100)
        button=QPushButton("Save",self)
        button.move(150,130)
        button.clicked.connect(self.getValue) #아래의 getValue 메소드를 호출한다
        self.combo.addItem("Python") #콤보박스에 값을 하나 추가할때는 addItem을 사용한다
        self.combo.addItems(["C","C#","PHP"]) #여러개를 추가할때는 addItems 를 사용하고 리스트로 넣는다
        list1=["Batman","Superman","Spiderman"]# 리스트를 먼저 만들고

        for name in list1: #반복문을 이용하여 addItem으로 하나씩 집어넣는다
            self.combo.addItem(name)

        for number in range(18,101): #반복문을 사용하여 숫자를 하나씩 addItem 을 한다
            self.combo.addItem(str(number)) #combo에는 숫자가 못들어간다 string으로 바꿔줘야한다


        self.show()

    def getValue(self):
        value=self.combo.currenttext1()
        print(value)

def main():
    App = QApplication(sys.argv)
    window=Window()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()