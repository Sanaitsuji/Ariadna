# -*- codingÑ utf-8 -*-
# -----------------------------
# Name: Tutorial
# Author: Oscar Velasco
# Creation: 18/05/2020
# Modified: 18/05/2020
# ------------------------------

__version__ = "1.0"

"""
Here you will find the design for the tutorial screen
"""

# Imports
from PyQt5.QtGui import QIcon, QPalette, QColor, QPixmap, QFont, QBrush, QImage
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtWidgets import QMainWindow, QFrame, QLabel, QLineEdit, QPushButton, QMessageBox
from src.controller import database
from src.views import main_menu


# ----------------- Windows Class ---------------


class WindowTutorial(QMainWindow):

    # ----------- Init Method ------------

    def __init__(self, parent=None):

        super(WindowTutorial, self).__init__(parent)

        self.setWindowTitle("Tutorial")
        self.setWindowIcon(QIcon("./images/LoginIcon.png"))
        self.setWindowFlags(Qt.WindowCloseButtonHint | Qt.MSWindowsFixedSizeDialogHint)
        self.setFixedSize(800, 720)

        oImage = QImage("./images/AriadnaTutorial.jpg")
        sImage = oImage.scaled(QSize(800, 720))
        palette_image = QPalette()
        palette_image.setBrush(QPalette.Window, QBrush(sImage))
        self.setPalette(palette_image)

        self.initui()

    # --------------- Window Widgets ----------

    def initui(self):

        palette = QPalette()
        palette.setColor(QPalette.Background, QColor(100, 100, 100))

        # ************ Header ************
        # ------------ Frame ----------
        frame = QFrame(self)
        frame.setFrameShape(QFrame.NoFrame)
        frame.setFrameShadow(QFrame.Sunken)
        frame.setAutoFillBackground(True)
        frame.setPalette(palette)
        frame.setFixedWidth(800)
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

        # ************ Body ************
        # ------------ Frame ----------
        instructions_frame = QFrame(self)
        instructions_frame.setFrameShape(QFrame.NoFrame)
        instructions_frame.setFrameShadow(QFrame.Sunken)
        instructions_frame.setAutoFillBackground(False)
        instructions_frame.setFixedWidth(300)
        instructions_frame.setFixedHeight(500)
        instructions_frame.move(0, 84)

        # ---------- Instructions ----------

        instructions_font = QFont()
        instructions_font.setPointSize(9)

        instructions_label = QLabel("<font style='font-family:times new roman;font-size:15px;' color='white'><b> "
                                    "<br/>Pre-resquisitos:"
                                    "<br/><br/>Para que la imagen pueda ser "
                                    "<br/>reconocida por el sistema, el "
                                    "<br/>laberinto debe ser dibujado en "
                                    "<br/>una hoja blanca con un marcador o"
                                    "<br/>esfero de color negro y debe tener"
                                    "<br/>una forma rectangular."
                                    "<br/><br/>Pasos:"
                                    "<br/><br/>1. Seleccionar la opcion "
                                    "<br/>'Nuevo Laberinto'."
                                    "<br/><br/>2. Seleccionar la opcion "
                                    "<br/>'Cargar laberinto', en esta opcion se."
                                    "<br/>soluciona el laberinto de manera "
                                    "<br/>automatica."
                                    "</b></font>",
                                    instructions_frame)
        instructions_label.setFont(instructions_font)
        instructions_label.move(20, 20)

        # ---------- Buttons ----------

        back_main_menu_button = QPushButton("Volver al Menu Principal", self)
        back_main_menu_button.setFixedWidth(200)
        back_main_menu_button.setFixedHeight(28)
        back_main_menu_button.move(300, 660)

        # ---------- Button's Events ----------

        back_main_menu_button.clicked.connect(self.back_main_menu)

    # --------------- Actions ----------

    def back_main_menu(self):

        self.window_main_menu = main_menu.WindowMainMenu()
        self.window_main_menu.show()
        self.hide()
