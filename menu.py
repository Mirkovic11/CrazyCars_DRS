from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap, QImage, QPalette, QBrush
from PyQt5.QtCore import QSize
from PyQt5 import QtCore, QtGui, QtWidgets
import sys, random

from Game import Game
from GameOverScreen import GameOverScreen

class UI(QtWidgets.QWidget):

    def init(self):
        self.i = 2
        self.StackedWidgets = QStackedWidget()
        self.home = QWidget()

        self.MenuUI()
        self.gameOverScreen = GameOverScreen()
        self.gameOverScreen.buttonRet.clicked.connect(lambda: self.gameOverScreen.returnHome(self.StackedWidgets))

        self.instructions = Instructions()
        self.instructions.buttonRet.clicked.connect(lambda: self.instructions.returnHome(self.StackedWidgets))

        self.StackedWidgets.addWidget(self.home)
        self.StackedWidgets.addWidget(self.instructions)
        self.StackedWidgets.addWidget(self.gameOverScreen)

    def SetGame(self):
        self.i = self.i +1
        self.player1 = "Plavi"
        self.player2 = "Crveni"
        self.game = Game(self.StackedWidgets, self.gameOverScreen, self.player1, self.player2, self)
        self.StackedWidgets.addWidget(self.game)
        self.StackedWidgets.setCurrentIndex(self.i)

    def getWinner(self, playerWinner):
        print ("Winner is: " + playerWinner)
        


    def MenuUI(self):
        self.home.setFixedSize(1200, 850)

        layout = QHBoxLayout()

        oImage = QImage("Slike/background.png")
        sImage = oImage.scaled(QSize(1200, 928))  # resize Image to widgets size
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(sImage))
        self.setPalette(palette)

        self.combo = QComboBox(self)
        self.igraci = 2
        self.combo.addItem("2 players")
        self.combo.addItem("4 players")
        self.combo.addItem("8 players")
        self.combo.activated[str].connect(self.selectionchange)
        layout.addWidget(self.combo)

        self.btn1 = QPushButton('Play', self.home)
        self.btn2 = QPushButton('Instructions', self.home)
        self.btn3 = QPushButton('High Score', self.home)

        self.btn1.setFixedSize(200, 80)
        self.btn2.setFixedSize(200, 80)
        self.btn3.setFixedSize(200, 80)
        layout.addWidget(self.btn1)
        layout.addWidget(self.btn2)
        layout.addWidget(self.btn3)
        layout.setAlignment(QtCore.Qt.AlignCenter)

        self.home.setLayout(layout)

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def selectionchange(self, text):
        if text == "2 players":
            self.igraci = 2
        elif text == "4 players":
            self.igraci = 4
        else:
            self.igraci = 8


class Instructions(QWidget):
    def __init__(self,):
        super().__init__()
        self.setFixedSize(900, 600)

        self.setStyleSheet("background-image: url(Slike/instructions.png)")

        self.buttonRet = QPushButton('',self)
        self.buttonRet.setFixedSize(517, 630)

        layout = QHBoxLayout()
        layout.addWidget(self.buttonRet)
        self.setLayout(layout)

    def returnHome(self, sw):
        sw.setCurrentIndex(0)
