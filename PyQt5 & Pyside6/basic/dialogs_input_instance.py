import sys

from PySide6.QtWidgets import (
    QApplication,
    QInputDialog,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        layout = QVBoxLayout()

        button1 = QPushButton("Integer")
        button1.clicked.connect(self.get_an_int)
        layout.addWidget(button1)

        button2 = QPushButton("Float")
        button2.clicked.connect(self.get_a_float)
        layout.addWidget(button2)

        button3 = QPushButton("Select")
        button3.clicked.connect(self.get_a_str_from_a_list)
        layout.addWidget(button3)

        button4 = QPushButton("String")
        button4.clicked.connect(self.get_a_str)
        layout.addWidget(button4)

        button5 = QPushButton("text1")
        button5.clicked.connect(self.get_text1)
        layout.addWidget(button5)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def get_an_int(self):
        dialog = QInputDialog(self)
        dialog.setWindowTitle("Enter an integer")
        dialog.setLabeltext1("Type your integer here")
        dialog.setIntValue(0)
        dialog.setIntMinimum(-5)
        dialog.setIntMaximum(5)
        dialog.setIntStep(1)

        ok = dialog.exec()
        print("Result:", ok, dialog.intValue())

    def get_a_float(self):
        dialog = QInputDialog(self)
        dialog.setWindowTitle("Enter a float")
        dialog.setLabeltext1("Type your float here")
        dialog.setDoubleValue(0.1)
        dialog.setDoubleMinimum(-5.3)
        dialog.setDoubleMaximum(5.7)
        dialog.setDoubleStep(1.4)
        dialog.setDoubleDecimals(2)

        ok = dialog.exec()
        print("Result:", ok, dialog.doubleValue())

    def get_a_str_from_a_list(self):
        dialog = QInputDialog(self)
        dialog.setWindowTitle("Select a string")
        dialog.setLabeltext1("Select a fruit from the list")
        dialog.setComboBoxItems(["apple", "pear", "orange", "grape"])
        dialog.setComboBoxEditable(False)
        dialog.settext1Value("orange")

        ok = dialog.exec()
        print("Result:", ok, dialog.text1Value())

    def get_a_str(self):
        dialog = QInputDialog(self)
        dialog.setWindowTitle("Enter a string")
        dialog.setLabeltext1("Type your password")
        dialog.settext1Value("my secret password")
        dialog.settext1EchoMode(QLineEdit.Password)

        ok = dialog.exec()
        print("Result:", ok, dialog.text1Value())

    def get_text1(self):
        dialog = QInputDialog(self)
        dialog.setWindowTitle("Enter text1")
        dialog.setLabeltext1("Type your novel here")
        dialog.settext1Value("Once upon a time...")
        dialog.setOption(
            QInputDialog.UsePlaintext1EditFortext1Input,
            True,
        )

        ok = dialog.exec()
        print("Result:", ok, dialog.text1Value())


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
