# -*- codingÑ utf-8 -*-
# -----------------------------
# Name: New Labyrinth
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
from PyQt5.QtWidgets import QMainWindow, QFrame, QLabel, QLineEdit, QPushButton, QMessageBox, QFileDialog
import psycopg2laberinto
from PIL import Image
import numpy as np
from src.controller import database
from src.views import main_menu


# ----------------- Windows Class ---------------


class WindowNewLabyrinth(QMainWindow):

    # ----------- Init Method ------------

    def __init__(self, parent=None):

        super(WindowNewLabyrinth, self).__init__(parent)

        self.setWindowTitle("Nuevo Laberinto")
        self.setWindowIcon(QIcon("./images/LoginIcon.png"))
        self.setWindowFlags(Qt.WindowCloseButtonHint | Qt.MSWindowsFixedSizeDialogHint)
        self.setFixedSize(800, 720)

        oImage = QImage("./images/AriadnaNewLab.jpg")
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

        # ------------ Labyrinth Frame ----------
        labyrinth_frame = QFrame(self)
        labyrinth_frame.setFrameShape(QFrame.NoFrame)
        labyrinth_frame.setFrameShadow(QFrame.Sunken)
        labyrinth_frame.setAutoFillBackground(False)
        labyrinth_frame.setPalette(palette)
        labyrinth_frame.setFixedWidth(800)
        labyrinth_frame.setFixedHeight(500)
        labyrinth_frame.move(0, 150)

        # ------------ Labyrinth ----------

        self.labyrinth_label = QLabel("", labyrinth_frame)
        self.labyrinth_label.setPixmap(QPixmap("./images/AriadnaFile.jpg"))
        self.labyrinth_label.setFixedWidth(420)
        self.labyrinth_label.setFixedHeight(280)
        self.labyrinth_label.setScaledContents(True)
        self.labyrinth_label.move(200, 100)

        # ---------- Buttons ----------

        load_labyrinth_button = QPushButton("Cargar Laberinto", self)
        load_labyrinth_button.setFixedWidth(175)
        load_labyrinth_button.setFixedHeight(28)
        load_labyrinth_button.move(60, 90)

        solve_labyrinth_button = QPushButton("Solucionar Laberinto", self)
        solve_labyrinth_button.setFixedWidth(175)
        solve_labyrinth_button.setFixedHeight(28)
        solve_labyrinth_button.move(315, 90)

        save_labyrinth_button = QPushButton("Guardar Laberinto", self)
        save_labyrinth_button.setFixedWidth(175)
        save_labyrinth_button.setFixedHeight(28)
        save_labyrinth_button.move(565, 90)

        back_main_menu_button = QPushButton("Menu Principal", self)
        back_main_menu_button.setFixedWidth(175)
        back_main_menu_button.setFixedHeight(28)
        back_main_menu_button.move(320, 680)

        # ---------- Button's Events ----------

        load_labyrinth_button.clicked.connect(self.load_labyrinth)
        solve_labyrinth_button.clicked.connect(self.solve_labyrinth)
        save_labyrinth_button.clicked.connect(self.save_labyrinth)
        back_main_menu_button.clicked.connect(self.back_main_menu)

    # --------------- Actions ----------

    def load_labyrinth(self):

        imagePath, _ = QFileDialog.getOpenFileName()
        image = Image.open(imagePath)
        image.thumbnail((420, 280))
        solution_image = image.convert('RGB')

        width = solution_image.width
        height = solution_image.height

        ways = {}

        start = ""
        points = self.get_points_labyrinth(solution_image, width, height, ways)
        for point in points.keys():
            if points[point] == 'Start':
                start = point

        path = []
        tried = []
        if start:
            find_exit = self.solve_labyrinth(start, points, path, tried, solution_image)
        else:
            find_exit = self.solve_labyrinth("0 0", points, path, tried, solution_image)

        print("---------> PATH", path)

        if find_exit:
            for point in path:
                column_row = point.split(" ")
                point_color = (0, 0, 0)
                try:
                    solution_image.putpixel((int(column_row[0]), int(column_row[1]) - 1), point_color)
                    solution_image.putpixel((int(column_row[0]) - 1, int(column_row[1])), point_color)
                    solution_image.putpixel((int(column_row[0]) + 1, int(column_row[1])), point_color)
                    solution_image.putpixel((int(column_row[0]), int(column_row[1]) + 1), point_color)
                except Exception as inst:
                    print("--------------->", inst)

        solution_image.save('./images/image_with_solution.jpg')

        pixmap = QPixmap('./images/image_with_solution.jpg')
        self.labyrinth_label.setPixmap(pixmap)
        self.image_labyrinth = image
        self.solution_labyrinth = solution_image

    def validate_color_labyrinth(self, solution_image, column, row):
        cont_color = 0
        pixel_color = solution_image.getpixel((column, row))
        if pixel_color == solution_image.getpixel((419, 195)):
            return "End"
        if pixel_color == solution_image.getpixel((4, 13)):
            return "Start"
        for color_labyrinth in pixel_color:
            if color_labyrinth == 255:
                cont_color += 1
        if cont_color == 3:
            return "Empty"
        elif pixel_color == (0, 0, 0):
            return False
        else:
            return True

    def get_points_labyrinth(self, solution_image, width, height, way):
        for column in range(width):
            for row in range(height):
                if row % 13 == 0 and (column % 12 == 0 or column == 4 or column == 419):
                    color_labyrinth = self.validate_color_labyrinth(solution_image, column, row)
                    if color_labyrinth in ["Empty", "End", "Start"]:
                        way[str(column) + " " + str(row)] = color_labyrinth
        return way

    def solve_labyrinth(self, point_start, points, path, tried, solution_image):
        column_row = point_start.split(" ")
        actual_column = int(column_row[0])
        actual_row = int(column_row[1])
        if points[point_start] == 'Empty' and point_start in tried:
            return False
        if points[point_start] == 'End':
            path.append(point_start)
            return True
        tried.append(point_start)

        if points[point_start] == 'Start':
            up = str(actual_column) + " " + str(actual_row - 13)
            down = str(actual_column) + " " + str(actual_row + 13)
            right = str(actual_column + 8) + " " + str(actual_row)
            up_validation = False
            down_validation = False
            right_validation = False
            if up in points.keys():
                up_validation = self.solve_labyrinth(up, points, path, tried, solution_image)
            if down in points.keys():
                down_validation = self.solve_labyrinth(down, points, path, tried, solution_image)
            if right in points.keys():
                right_validation = self.solve_labyrinth(right, points, path, tried, solution_image)
            find_exit = up_validation or down_validation or right_validation
        else:
            if actual_column == 408 and actual_row == 195:
                right = str(actual_column + 11) + " " + str(actual_row)
            else:
                right = str(actual_column + 12) + " " + str(actual_row)
            up = str(actual_column) + " " + str(actual_row - 13)
            down = str(actual_column) + " " + str(actual_row + 13)
            left = str(actual_column - 12) + " " + str(actual_row)
            up_validation = False
            down_validation = False
            right_validation = False
            right_between = ""
            left_validation = False
            if up in points.keys():
                up_validation = self.solve_labyrinth(up, points, path, tried, solution_image)
            if down in points.keys():
                down_validation = self.solve_labyrinth(down, points, path, tried, solution_image)
            if right in points.keys():
                right_between = self.validate_color_labyrinth(solution_image, actual_column+6, actual_row)
                right_validation = self.solve_labyrinth(right, points, path, tried, solution_image)
            if left in points.keys():
                left_validation = self.solve_labyrinth(left, points, path, tried, solution_image)
            find_exit = up_validation or down_validation or left_validation or right_validation

        if find_exit:
            path.append(point_start)

        return find_exit


    def save_labyrinth(self):
        binary = psycopg2.Binary(self.image_labyrinth)

        print("---------------> SAVE LABYRINTH")

    def back_main_menu(self):

        self.window_main_menu = main_menu.WindowMainMenu()
        self.window_main_menu.show()
        self.hide()

