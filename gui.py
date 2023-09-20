from PySide6.QtCore import Qt, QSize
from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QLabel, QGridLayout, QStackedWidget,\
    QVBoxLayout, QHBoxLayout
from PySide6.QtGui import QPixmap, QIcon, QFont, QLinearGradient, QColor, QImage, QFontDatabase, QPalette
import random as rd
import requests




class Window(QMainWindow):

    def __init__(self):
        super().__init__()
        #self.setFixedSize(QSize(1000, 600))
        self.setWindowTitle("Quizzard")
        self.main_widget = QWidget()
        self.setCentralWidget(self.main_widget)
        #self.setStyleSheet('background-color: white;')

        gradient = QLinearGradient(0, 0, 0, self.height())
        gradient.setColorAt(0, QColor("#7b50bf"))
        gradient.setColorAt(1, QColor("#22c1c3"))
        palette = self.palette()
        palette.setBrush(QPalette.Window, gradient)
        self.setPalette(palette)

        layout = QGridLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        self.main_widget.setLayout(layout)

        self.stacked_widgets = QStackedWidget()
        layout.addWidget(self.stacked_widgets)

        main_page = EntryPage()
        layout.addWidget(main_page)


# --------------------------------------------------------------- MAIN PAGE
class EntryPage(QWidget):

    def __init__(self):
        super().__init__()

        QFontDatabase.addApplicationFont('fonts/lobster.ttf')

        self.setFixedSize(QSize(800, 600))

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignHCenter)
        layout.setSpacing(0)
        layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(layout)

        pixmap = QPixmap().fromImage(QImage('images/logo.png'))
        label = QLabel()
        label.setContentsMargins(0, 0, 0, 0)
        label.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignHCenter)
        label.setPixmap(pixmap)

        app_name_label = QLabel("Quizzard")
        app_name_label.setContentsMargins(0, 0, 0, 50)
        app_name_label.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignHCenter)
        app_name_label.setFont(QFont("Lobster", 50))
        app_name_label.setStyleSheet("color: #5d0fd8;")

        category_label = QLabel("Choose category:")
        category_label.setContentsMargins(0, 0, 0, 10)
        category_label.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignHCenter)
        category_label.setFont(QFont("Lobster", 20))
        category_label.setStyleSheet("color: #5d0fd8;")

        cat_1 = CategoryButton("Sports")
        cat_2 = CategoryButton("Art")
        cat_3 = CategoryButton("General")
        cat_4 = CategoryButton("Mathematics")
        cat_5 = CategoryButton("Geography")
        cat_6 = CategoryButton("Video Games")

        col_1 = QVBoxLayout()
        col_2 = QVBoxLayout()

        col_1.addWidget(cat_1)
        col_1.addWidget(cat_2)
        col_1.addWidget(cat_5)
        col_2.addWidget(cat_3)
        col_2.addWidget(cat_4)
        col_2.addWidget(cat_6)

        row = QHBoxLayout()
        row.setSpacing(50)
        row.setContentsMargins(0, 0, 0, 0)
        row.addLayout(col_1)
        row.addLayout(col_2)

        layout.addWidget(app_name_label)
        layout.addWidget(category_label)
        layout.addLayout(row)


# --------------------------------------------------------------- QUIZ PAGE
class QuizPage(QWidget):

    def __init__(self):
        super().__init__()
        self.setFixedSize(QSize(800, 600))

        layout = QGridLayout()
        self.setLayout(layout)



class CategoryButton(QPushButton):

    def __init__(self, text):
        super().__init__()
        self.setText(text)
        self.setFixedSize(QSize(150, 100))
        self.setStyleSheet("""  background-color: beige;
                                border-style: outset;
                                border-width: 4px;
                                border-radius: 50px;
                                border-color: #5d0fd8;
                                font: bold 14px;
                                min-width: 10em;
                                padding: 6px;
                                color: #5d0fd8;""")
        font = QFont('Lobster')

        self.setFont(font)













