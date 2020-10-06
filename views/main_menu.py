# -*- codingÑ utf-8 -*-
# -----------------------------
# Name: Main Menu
# Author: Oscar Velasco
# Creation: 18/05/2020
# Modified: 18/05/2020
# ------------------------------

__version__ = "1.0"

"""
Here you will find the design for the main menu screen
"""

# Imports
from PyQt5.QtGui import QIcon, QPalette, QColor, QPixmap, QFont, QBrush, QImage
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtWidgets import QMainWindow, QFrame, QLabel, QLineEdit, QPushButton, QMessageBox
from src.controller import database
from src.views import login, tutorial, new_labyrinth


# ----------------- Windows Class ---------------


class WindowMainMenu(QMainWindow):

    # ----------- Init Method ------------

    def __init__(self, parent=None):

        super(WindowMainMenu, self).__init__(parent)

        self.setWindowTitle("Menu Principal")
        self.setWindowIcon(QIcon("./images/LoginIcon.png"))
        self.setWindowFlags(Qt.WindowCloseButtonHint | Qt.MSWindowsFixedSizeDialogHint)
        self.setFixedSize(500, 480)

        oImage = QImage("./images/AriadnaMainMenu.jpg")
        sImage = oImage.scaled(QSize(500, 480))
        palette_image = QPalette()
        palette_image.setBrush(QPalette.Window, QBrush(sImage))
        self.setPalette(palette_image)

        self.initui()

    # --------------- Window Widgets ----------

    def initui(self):

        print("---------> USER", login.USER)

        palette = QPalette()
        palette.setColor(QPalette.Background, QColor(100, 100, 100))

        # ************ Header ************
        # ------------ Frame ----------
        frame = QFrame(self)
        frame.setFrameShape(QFrame.NoFrame)
        frame.setFrameShadow(QFrame.Sunken)
        frame.setAutoFillBackground(True)
        frame.setPalette(palette)
        frame.setFixedWidth(500)
        frame.setFixedHeight(84)
        frame.move(0, 0)

        # ------------ Icon ----------

        label_icon = QLabel(frame)
        label_icon.setFixedWidth(40)
        label_icon.setFixedHeight(40)
        label_icon.setPixmap(QPixmap("./images/LoginIcon.png").scaled(40, 40, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        label_icon.move(57, 22)

        # ------------ Tittle ----------

        tittle_font = QFont()
        tittle_font.setPixelSize(16)
        tittle_font.setBold(True)

        tittle_label = QLabel("<font color='white'> Ariadna </rfont>", frame)
        tittle_label.setFont(tittle_font)
        tittle_label.move(103, 20)

        # ------------ Sub Tittle ----------

        sub_tittle_font = QFont()
        sub_tittle_font.setPointSize(9)

        sub_tittle_label = QLabel("<font color='white'> Labyrinth Solver </font>", frame)
        sub_tittle_label.setFont(sub_tittle_font)
        sub_tittle_label.move(111, 46)

        # ---------- Buttons ----------

        tutorial_button = QPushButton("Tutorial", self)
        tutorial_button.setFixedWidth(175)
        tutorial_button.setFixedHeight(28)
        tutorial_button.move(10, 90)

        new_labyrinth_button = QPushButton("Nuevo Laberinto", self)
        new_labyrinth_button.setFixedWidth(175)
        new_labyrinth_button.setFixedHeight(28)
        new_labyrinth_button.move(10, 160)

        """my_labyrinths_button = QPushButton("Mis Laberintos", self)
        my_labyrinths_button.setFixedWidth(175)
        my_labyrinths_button.setFixedHeight(28)
        my_labyrinths_button.move(10, 160)"""

        login_button = QPushButton("Cerrar Sesion", self)
        login_button.setFixedWidth(175)
        login_button.setFixedHeight(28)
        login_button.move(10, 190)

        # ---------- Button's Events ----------

        tutorial_button.clicked.connect(self.tutorial)
        """my_labyrinths_button.clicked.connect(self.my_labyrinths)"""
        new_labyrinth_button.clicked.connect(self.new_labyrinth)
        login_button.clicked.connect(self.login)

    # --------------- Actions ----------

    def tutorial(self):

        self.window_tutorial = tutorial.WindowTutorial()
        self.window_tutorial.show()
        self.hide()

    def new_labyrinth(self):

        self.window_new_labyrinth = new_labyrinth.WindowNewLabyrinth()
        self.window_new_labyrinth.show()
        self.hide()

    def my_labyrinths(self):
        print("---------------> MY LABYRINTHS")

    def login(self):

        self.window_login = login.WindowLogin()
        self.window_login.show()
        self.hide()
