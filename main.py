# -*- codingÑ utf-8 -*-
# -----------------------------
# Name: Main
# Author: Oscar Velasco
# Creation: 18/05/2020
# Modified: 18/05/2020
# ------------------------------

__version__ = "1.0"

"""
Main method to execute the program
"""

from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication
from src.views import login, main_menu

# ============== MAIN ===============

if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)

    font = QFont()
    font.setPointSize(10)
    font.setFamily("Bahnschrift Light")

    app.setFont(font)

    window = login.WindowLogin()
    #window = main_menu.WindowMainMenu()
    window.show()

    sys.exit(app.exec_())
