# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 17:17:52 2021

@author: Spark
"""

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont,QPixmap
from PyQt5.QtCore import QTimer
from random import randint


text1Font=QFont("Times",14)
buttonFont=QFont("Arial",12)
computerScore=0
playerScore=0


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("가위 바위 보")
        self.setGeometry(350,150,550,500)
        self.UI()


    def UI(self):
        #############################Scores####################
        self.scoreComputertext1=QLabel("Computer Score : ",self)
        self.scoreComputertext1.move(30,20)
        self.scoreComputertext1.setFont(text1Font)
        self.scorePlayertext1=QLabel("Your Score : ",self)
        self.scorePlayertext1.setFont(text1Font)
        self.scorePlayertext1.move(330,20)
        ###########################Images########################
        self.imageComputer=QLabel(self)
        self.imageComputer.setPixmap(QPixmap("rock.png"))
        self.imageComputer.move(50,100)

        self.imagePlayer = QLabel(self)
        self.imagePlayer.setPixmap(QPixmap("rock.png"))
        self.imagePlayer.move(330, 100)

        self.imageGame=QLabel(self)
        self.imageGame.setPixmap(QPixmap("game.png"))
        self.imageGame.move(230,160)
        #####################Buttons######################
        btnStart=QPushButton("Start",self)
        btnStart.setFont(buttonFont)
        btnStart.move(180,250)
        btnStart.clicked.connect(self.start)
        btnStop=QPushButton("Stop",self)
        btnStop.setFont(buttonFont)
        btnStop.clicked.connect(self.stop)
        btnStop.move(270,250)
        ###########################Timer##################

        self.timer=QTimer(self)
        self.timer.setInterval(500)
        self.timer.timeout.connect(self.playGame)

        self.show()

    def start(self):
        self.timer.start()

    def playGame(self):
        self.rndComputer=randint(1, 3)
        self.rndPlayer = randint(1, 3)
        print(self.rndPlayer,self.rndComputer)

        if self.rndComputer == 1:
            self.imageComputer.setPixmap(QPixmap("rock.png"))
        elif self.rndComputer == 2:
            self.imageComputer.setPixmap(QPixmap("paper.png"))
        else:
            self.imageComputer.setPixmap(QPixmap("scissors.png"))


        if self.rndPlayer == 1:
            self.imagePlayer.setPixmap(QPixmap("rock.png"))

        elif self.rndPlayer == 2:
            self.imagePlayer.setPixmap(QPixmap("paper.png"))
        else:
            self.imagePlayer.setPixmap(QPixmap("scissors.png"))




    def stop(self):
        global computerScore
        global playerScore
        self.timer.stop()

        if self.rndComputer == 1 and self.rndPlayer == 1:
            mbox=QMessageBox.information(self,"Information","Draw Game")

        elif self.rndComputer== 1 and self.rndPlayer == 2:
            mbox=QMessageBox.information(self,"Information","You Win")
            playerScore +=1
            self.scorePlayertext1.settext1("Your Score:{}".format(playerScore))
        elif self.rndComputer == 1 and self.rndPlayer == 3:
            mbox = QMessageBox.information(self, "Information", "Computer Wins")
            computerScore +=1
            self.scoreComputertext1.settext1("Computer Score:{}".format(computerScore))

        elif self.rndComputer == 2 and self.rndPlayer ==1:
            mbox = QMessageBox.information(self, "Information", "Computer Wins")
            computerScore += 1
            self.scoreComputertext1.settext1("Computer Score:{}".format(computerScore))
        elif self.rndComputer == 2 and self.rndPlayer ==2:
            mbox=QMessageBox.information(self,"Information","Draw Game")

        elif self.rndComputer == 2 and self.rndPlayer == 3:
            mbox = QMessageBox.information(self, "Information", "You Win")
            playerScore += 1
            self.scorePlayertext1.settext1("Your Score:{}".format(playerScore))

        elif self.rndComputer == 3 and self.rndPlayer == 1:
            mbox = QMessageBox.information(self, "Information", "You Win")
            playerScore += 1
            self.scorePlayertext1.settext1("Your Score:{}".format(playerScore))
        elif self.rndComputer == 3 and self.rndPlayer ==2:
            mbox = QMessageBox.information(self, "Information", "Computer Wins")
            computerScore += 1
            self.scoreComputertext1.settext1("Computer Score:{}".format(computerScore))
        elif self.rndComputer == 3 and self.rndPlayer == 3:
            mbox = QMessageBox.information(self, "Information", "Draw Game")

        if computerScore == 3 or playerScore ==3 :
            mbox=QMessageBox.information(self,"Information","Game Over")
            sys.exit()


def main():
    App = QApplication(sys.argv)
    window = Window()
    window.start()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()