# -*- codingÑ utf-8 -*-
# -----------------------------
# Name: Sign In
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
from src.views import login


# ----------------- Windows Class ---------------


class WindowSignIn(QMainWindow):

    # ----------- Init Method ------------

    def __init__(self, parent=None):

        super(WindowSignIn, self).__init__(parent)

        self.setWindowTitle("Ariadna Sign In")
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

        tittle_label = QLabel("<font color='white'> Ariadna Sign In </rfont>", frame)
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
        user_label.move(90, 110)

        user_frame = QFrame(self)
        user_frame.setFrameShape(QFrame.StyledPanel)
        user_frame.setFixedWidth(338)
        user_frame.setFixedHeight(28)
        user_frame.move(90, 136)

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
        password_label.move(90, 170)

        password_frame = QFrame(self)
        password_frame.setFrameShape(QFrame.StyledPanel)
        password_frame.setFixedWidth(338)
        password_frame.setFixedHeight(28)
        password_frame.move(90, 196)

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

        # ---------- Confirm Password ----------

        confirm_password_label = QLabel("Confirmar Contraseña", self)
        confirm_password_label.move(90, 224)

        confirm_password_frame = QFrame(self)
        confirm_password_frame.setFrameShape(QFrame.StyledPanel)
        confirm_password_frame.setFixedWidth(338)
        confirm_password_frame.setFixedHeight(28)
        confirm_password_frame.move(90, 250)

        confirm_password_icon = QLabel(confirm_password_frame)
        confirm_password_icon.setPixmap(QPixmap("./images/PasswordIcon.png").scaled(20, 20, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        confirm_password_icon.move(10, 4)

        self.line_edit_confirm_password = QLineEdit(confirm_password_frame)
        self.line_edit_confirm_password.setFrame(False)
        self.line_edit_confirm_password.setEchoMode(QLineEdit.Password)
        self.line_edit_confirm_password.setTextMargins(8, 0, 4, 1)
        self.line_edit_confirm_password.setFixedWidth(297)
        self.line_edit_confirm_password.setFixedHeight(26)
        self.line_edit_confirm_password.move(40, 1)

        # ---------- Buttons ----------

        sign_in_button = QPushButton("Registrarse", self)
        sign_in_button.setFixedWidth(175)
        sign_in_button.setFixedHeight(28)
        sign_in_button.move(170, 300)

        login_button = QPushButton("Volver a Login", self)
        login_button.setFixedWidth(175)
        login_button.setFixedHeight(28)
        login_button.move(170, 334)

        cancel_button = QPushButton("Cancelar", self)
        cancel_button.setFixedWidth(135)
        cancel_button.setFixedHeight(28)
        cancel_button.move(192, 368)

        # ---------- Button's Events ----------

        sign_in_button.clicked.connect(self.sign_in)
        login_button.clicked.connect(self.login)
        cancel_button.clicked.connect(self.close)

    # --------------- Actions ----------

    def sign_in(self):

        valid_creation = True

        database_object = database.Database()

        table = "user"
        columns = ['id', 'name', 'password']

        max_id = database_object.get_last_id(table)

        user = self.line_edit_user.text()
        password = self.line_edit_password.text()
        confirm_password = self.line_edit_confirm_password.text()

        if not user or not password or not confirm_password:
            valid_creation = False
            QMessageBox.about(self, "Error", "Diligencie todos lo campos para continuar con el registro.")

        if len(user) > 13 and valid_creation:
            valid_creation = False
            QMessageBox.about(self, "Error", "El nombre de usuario debe tener maximo 13 caracteres.")

        if len(password) > 13 and valid_creation:
            valid_creation = False
            QMessageBox.about(self, "Error", "La contraseña debe tener maximo 13 caracteres.")

        if password != confirm_password and valid_creation:
            valid_creation = False
            QMessageBox.about(self, "Error", "Los campos Contraseña y Confirmar Contraseña no coinciden.")

        search_id = database_object.search("id", table, ['name'], [user], "text")
        if search_id and valid_creation:
            valid_creation = False
            QMessageBox.about(self, "Error", "Este nombre de usuario ya esta en uso.")

        if valid_creation:
            ariadna_id = max_id[0] + 1
            values = [ariadna_id, user, password]
            # print("Id:", ariadna_id)
            # print("User:", user)
            # print("Password:", password)
            # print("Confirm Password:", confirm_password)

            database_object.create(table, columns, values)

            QMessageBox.about(self, "Creacion", "Usuario creado con exito.")

            self.login()

    def login(self):

        self.window_login = login.WindowLogin()
        self.window_login.show()
        self.hide()

