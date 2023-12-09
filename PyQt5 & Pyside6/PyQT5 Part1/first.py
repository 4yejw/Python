# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 11:24:49 2021

@author: Spark
"""

import sys
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Using Labels") #좌상단 제목
        self.setGeometry(150, 150, 500, 350)  # 모니터 좌상단기준 150 150픽셀 이동

        #위젯 : 윈도우 안에 들어가는 기능들


        self.show()  # 화면에 띄워준다


def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())


if __name__ == '__main__':
    main()
