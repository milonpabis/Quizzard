from gui import Window, QApplication
from brain import GameBrain


#todo:
# - question pages
# - app brain
# - connect brain with gui





if __name__ == "__main__":
    app = QApplication()
    window = Window()
    window.show()
    app.exec()
    # brain = GameBrain('Sports').return_question()
    # print(next(brain))





