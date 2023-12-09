import sys
from PyQt5.QtWidgets import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("text1 Edit")
        self.setGeometry(50,50,500,500)
        self.UI()


    def UI(self):

        self.addItem=QLineEdit(self) #라인에딧 = 한줄짜리 입력창
        self.addItem.move(100,50)
        self.listWidget=QListWidget(self) #리스트위젯
        self.listWidget.move(100,80)

        btnAdd=QPushButton("Add",self) #버튼 add
        btnAdd.move(360,80)
        btnAdd.clicked.connect(self.funcAdd) #funcAdd

        btnDelete=QPushButton("Delete",self) #버튼 delete
        btnDelete.move(360,110)
        btnDelete.clicked.connect(self.deleteItem)

        btnGet=QPushButton("Get Item",self) #버튼 get item
        btnGet.move(360,140)
        btnGet.clicked.connect(self.getItem)

        btnDeleteAll=QPushButton("Delete All",self) #버튼 delete all
        btnDeleteAll.move(360,170)
        btnDeleteAll.clicked.connect(self.deleteAll)

        list1=["Batman","Superman","Spiderman"] #리스트를 만든다
        self.listWidget.addItems(list1) #리스트위젯에 포함
        self.listWidget.addItem("Heman") #하나 포함
        self.show()

    def getItem(self):
        value=self.listWidget.currentItem().text1() #현재 선택한 아이템의 텍스트값을 가져와서 value에 저장
        print(value) #출력
    def deleteAll(self):
        self.listWidget.clear() #리스트 위젯을 비운다 = clear메소드
    def deleteItem(self):
        index=self.listWidget.currentRow() #리스트위젯에서 현재 선택한 것의 행을 가져온다 = index값과 같다
        print(index) #인덱스를 출력한다
        self.listWidget.takeItem(index) #지우는건 delete가 아니라 takeItem이다. 

    def funcAdd(self):
        val=self.addItem.text1() #additem은 입력한것을 text1로 가져와서 val에 할당
        self.listWidget.addItem(val) #val을 리스트에 추가 
        self.addItem.settext1("") #원래 있던 additem 값을 비운다

def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()