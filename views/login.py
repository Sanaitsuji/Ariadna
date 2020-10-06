# -*- codingÑ utf-8 -*-
# -----------------------------
# Name: Login
# Author: Oscar Velasco
# Creation: 18/05/2020
# Modified: 18/05/2020
# ------------------------------

__version__ = "1.0"

"""
Here you will find the design for the login screen
"""

# Imports
from PyQt5.QtGui import QIcon, QPalette, QColor, QPixmap, QFont
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QFrame, QLabel, QLineEdit, QPushButton, QMessageBox
from src.controller import database
from src.views import signin, main_menu
from src.models import user as user_class
import sys

USER = 12345

# ----------------- Windows Class ---------------


class WindowLogin(QMainWindow):

    # ----------- Init Method ------------

    def __init__(self, parent=None):

        super(WindowLogin, self).__init__(parent)

        self.setWindowTitle("Ariadna Login")
        self.setWindowIcon(QIcon("./images/LoginIcon.png"))
        self.setWindowFlags(Qt.WindowCloseButtonHint | Qt.MSWindowsFixedSizeDialogHint)
        self.setFixedSize(500, 480)

        palette = QPalette()
        palette.setColor(QPalette.Background, QColor(243, 243, 243))
        self.setPalette(palette)

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

        # ************ Login ************

        # ---------- User ----------

        user_label = QLabel('Usuario', self)
        user_label.move(90, 170)

        user_frame = QFrame(self)
        user_frame.setFrameShape(QFrame.StyledPanel)
        user_frame.setFixedWidth(338)
        user_frame.setFixedHeight(28)
        user_frame.move(90, 196)

        user_icon = QLabel(user_frame)
        user_icon.setPixmap(QPixmap("./images/UserIcon.png").scaled(20, 20, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        user_icon.move(10, 4)

        self.line_edit_user = QLineEdit(user_frame)
        self.line_edit_user.setFrame(False)
        self.line_edit_user.setTextMargins(8, 0, 4, 1)
        self.line_edit_user.setFixedWidth(297)
        self.line_edit_user.setFixedHeight(26)
        self.line_edit_user.move(40, 1)

        # ---------- Password ----------

        password_label = QLabel("Contraseña", self)
        password_label.move(90, 224)

        password_frame = QFrame(self)
        password_frame.setFrameShape(QFrame.StyledPanel)
        password_frame.setFixedWidth(338)
        password_frame.setFixedHeight(28)
        password_frame.move(90, 250)

        password_icon = QLabel(password_frame)
        password_icon.setPixmap(QPixmap("./images/PasswordIcon.png").scaled(20, 20, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        password_icon.move(10, 4)

        self.line_edit_password = QLineEdit(password_frame)
        self.line_edit_password.setFrame(False)
        self.line_edit_password.setEchoMode(QLineEdit.Password)
        self.line_edit_password.setTextMargins(8, 0, 4, 1)
        self.line_edit_password.setFixedWidth(297)
        self.line_edit_password.setFixedHeight(26)
        self.line_edit_password.move(40, 1)

        # ---------- Buttons ----------

        login_button = QPushButton("Iniciar Sesión", self)
        login_button.setFixedWidth(175)
        login_button.setFixedHeight(28)
        login_button.move(170, 290)

        signin_button = QPushButton("Registrarse", self)
        signin_button.setFixedWidth(175)
        signin_button.setFixedHeight(28)
        signin_button.move(170, 326)

        cancel_button = QPushButton("Cancelar", self)
        cancel_button.setFixedWidth(130)
        cancel_button.setFixedHeight(28)
        cancel_button.move(193, 362)

        # ---------- Button's Events ----------

        login_button.clicked.connect(self.login)
        cancel_button.clicked.connect(self.close)
        signin_button.clicked.connect(self.signin)

    # --------------- Actions ----------

    def login(self):
        valid_login = True
        database_object = database.Database()
        table = "user"

        # account = self.account_box.currentText()
        user = self.line_edit_user.text()
        password = self.line_edit_password.text()

        if not user or not password and valid_login:
            valid_login = False
            QMessageBox.about(self, "Error", "Diligencie todos lo campos para continuar con el registro.")

        search_id = database_object.search("id", table, ['name'], [user], "text")
        if not search_id and valid_login:
            valid_login = False
            QMessageBox.about(self, "Error", "No se encontro ningun usuario con el nombre especificado.")

        if search_id and valid_login:
            user_id = search_id[0]
            database_password = database_object.search("password", table, ['id'], [user_id], "num")
            if database_password[0] != password:
                QMessageBox.about(self, "Error", "Contraseña incorrecta.")
            else:
                user_obj = user_class.User()
                values = {
                    'id': search_id,
                    'name': user
                }
                global USER
                USER = user_obj.create(values)
                self.window_main_menu = user_obj.create(values)
                self.window_main_menu = main_menu.WindowMainMenu()
                self.window_main_menu.show()
                self.hide()

    def signin(self):
        self.window_sign_in = signin.WindowSignIn()
        self.window_sign_in.show()
        self.hide()
