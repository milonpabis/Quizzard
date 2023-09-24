from gui import Window, QApplication
from brain import GameBrain


#todo:
# - improve gui style
# - change API database
# - track best result ( sql ) // future





if __name__ == "__main__":
    app = QApplication()
    window = Window()
    window.show()
    app.exec()
    # brain = GameBrain('Sports').return_question()
    # print(next(brain))





