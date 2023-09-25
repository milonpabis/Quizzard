from gui import Window, QApplication
from brain import GameBrain


#todo:
# - improve GUI style ( COLORS, QUESTION LABEL, GRADIENT )
# - disable buttons after clicking x
# - give request 2seconds for getting the respond before starting GUI question page





if __name__ == "__main__":
    app = QApplication()
    window = Window()
    window.show()
    app.exec()
    # brain = GameBrain('Sports').return_question()
    # print(next(brain))





