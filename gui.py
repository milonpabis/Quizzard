from PySide6.QtCore import Qt, QSize
from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QLabel, QGridLayout, QStackedWidget,\
    QVBoxLayout, QHBoxLayout, QButtonGroup
from PySide6.QtGui import QPixmap, QIcon, QFont, QLinearGradient, QColor, QImage, QFontDatabase, QPalette
from brain import GameBrain
import random as rd





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

        self.main_page = EntryPage(self)
        self.question_page = QuizPage(self)
        self.end_page = EndPage(self)
        self.stacked_widgets.addWidget(self.main_page)
        self.stacked_widgets.addWidget(self.question_page)
        self.stacked_widgets.addWidget(self.end_page)


# --------------------------------------------------------------- MAIN PAGE
class EntryPage(QWidget):

    def __init__(self, main):
        super().__init__()

        QFontDatabase.addApplicationFont('fonts/lobster.ttf')

        self.setFixedSize(QSize(800, 600))
        self.data = None
        self.g_answer = None
        self.main = main

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

        self.cat_1 = CategoryButton("Sports")
        self.cat_2 = CategoryButton("Art")
        self.cat_3 = CategoryButton("General")
        self.cat_4 = CategoryButton("Mathematics")
        self.cat_5 = CategoryButton("Geography")
        self.cat_6 = CategoryButton("Video Games")

        self.button_group = QButtonGroup()
        self.button_group.addButton(self.cat_1)
        self.button_group.addButton(self.cat_2)
        self.button_group.addButton(self.cat_3)
        self.button_group.addButton(self.cat_4)
        self.button_group.addButton(self.cat_5)
        self.button_group.addButton(self.cat_6)

        self.button_group.buttonPressed.connect(self.choose_category)


        col_1 = QVBoxLayout()
        col_2 = QVBoxLayout()

        col_1.addWidget(self.cat_1)
        col_1.addWidget(self.cat_2)
        col_1.addWidget(self.cat_5)
        col_2.addWidget(self.cat_3)
        col_2.addWidget(self.cat_4)
        col_2.addWidget(self.cat_6)

        row = QHBoxLayout()
        row.setSpacing(50)
        row.setContentsMargins(0, 0, 0, 0)
        row.addLayout(col_1)
        row.addLayout(col_2)

        layout.addWidget(app_name_label)
        layout.addWidget(category_label)
        layout.addLayout(row)


    def choose_category(self, button):


        if button == self.cat_1:        # SPORTS
            self.data = GameBrain("Sports").return_question()
        elif button == self.cat_2:      # ART
            self.data = GameBrain("Art").return_question()
        elif button == self.cat_3:      # GENERAL
            self.data = GameBrain("General").return_question()
        elif button == self.cat_4:      # MATHEMATICS
            self.data = GameBrain("Mathematics").return_question()
        elif button == self.cat_5:      # GEOGRAPHY
            self.data = GameBrain("Geography").return_question()
        elif button == self.cat_6:      # VIDEO GAMES
            self.data = GameBrain("Video Games").return_question()

        self.next_question()
        self.main.stacked_widgets.setCurrentIndex(1)

    def next_question(self):
        if self.main.question_page.q_number <= 10:
            f_question = next(self.data)
            question = f_question[0]
            self.g_answer = f_question[1]
            answers = f_question[2] + [self.g_answer]
            rd.shuffle(answers)

            self.main.question_page.question.setText(question)
            self.main.question_page.but_1.setText(answers[0])
            self.main.question_page.but_2.setText(answers[1])
            self.main.question_page.but_3.setText(answers[2])
            self.main.question_page.but_4.setText(answers[3])
            self.main.question_page.question_number.setText(f"{self.main.question_page.q_number}/10")
        else:
            self.main.stacked_widgets.setCurrentIndex(2)
            self.main.end_page.points_collected.setText(f"Your result: {self.main.question_page.points}/10")


# --------------------------------------------------------------- QUIZ PAGE
class QuizPage(QWidget):

    def __init__(self, main):
        super().__init__()
        self.setFixedSize(QSize(800, 600))
        self.main = main
        self.points = 0
        self.q_number = 1

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.setLayout(layout)

        app_name_label = QLabel("Quizzard")
        app_name_label.setContentsMargins(0, 0, 0, 50)
        app_name_label.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignHCenter)
        app_name_label.setFont(QFont("Lobster", 50))
        app_name_label.setStyleSheet("color: #5d0fd8;")

        self.but_1 = CategoryButton('A: test1')
        self.but_2 = CategoryButton('B: test2')
        self.but_3 = CategoryButton('C: test3')
        self.but_4 = CategoryButton('D: test4')

        self.button_group = QButtonGroup()
        self.button_group.addButton(self.but_1)
        self.button_group.addButton(self.but_2)
        self.button_group.addButton(self.but_3)
        self.button_group.addButton(self.but_4)

        self.button_group.buttonPressed.connect(self.next_question)

        self.question = Question('TEST QUESTION ABCD OR SMTH ELSE?')

        self.question_number = QLabel(f"{self.q_number}/10")
        self.question_number.setFont(QFont("Lobster", 14))
        self.question_number.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.question_number.setStyleSheet("color: #5d0fd8;")


        col1 = QVBoxLayout()
        col2 = QVBoxLayout()

        col1.addWidget(self.but_1)
        col1.addWidget(self.but_2)
        col2.addWidget(self.but_3)
        col2.addWidget(self.but_4)

        row = QHBoxLayout()
        row.setContentsMargins(0, 20, 0, 100)
        row.setSpacing(25)

        row.addLayout(col1)
        row.addLayout(col2)

        layout.addWidget(app_name_label)
        layout.addWidget(self.question)
        layout.addLayout(row)
        layout.addWidget(self.question_number)




    def next_question(self, button):
        if button.text() == self.main.main_page.g_answer:
            self.points += 1
        self.q_number += 1
        self.main.main_page.next_question()



class EndPage(QWidget):

    def __init__(self, main):
        super().__init__()
        self.main = main
        self.setFixedSize(QSize(800, 600))

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.points_collected = QLabel("Your result: 0/10")
        self.points_collected.setStyleSheet("color: #5d0fd8;")
        self.points_collected.setFont(QFont("Lobster", 20))
        self.points_collected.setAlignment(Qt.AlignmentFlag.AlignCenter)

        new_game_button = CategoryButton("New Game")
        new_game_button.pressed.connect(self.new_game)
        exit_button = CategoryButton("Exit")
        exit_button.pressed.connect(self.exit)
        col = QVBoxLayout()
        col.addWidget(new_game_button)
        col.addWidget(exit_button)
        col.setAlignment(Qt.AlignmentFlag.AlignCenter)

        layout.addWidget(self.points_collected)
        layout.addLayout(col)


    def new_game(self):
        self.main.question_page.q_number = 1
        self.main.question_page.points = 0
        self.main.stacked_widgets.setCurrentIndex(0)

    def exit(self):
        self.main.destroy()


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


class Question(CategoryButton):

    def __init__(self, text):
        super().__init__(text)
        self.setFixedSize(QSize(500, 100))
        self.setEnabled(False)
