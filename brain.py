import requests
import random as rd

AMOUNT = 10
URL = f"https://opentdb.com/api.php?amount={AMOUNT}&category="
CATEGORIES_NUMS = {'Sports': '21', 'Mathematics': '19', 'General': '9', 'Art': '25', 'Video Games': '15',
                                   'Geography': '22'}


class GameBrain:

    def __init__(self, category):
        self.category = category
        self.respond = requests.get(URL + CATEGORIES_NUMS[category])
        print(self.respond.text)


    def return_question(self):

        for _ in range(AMOUNT):
            question = None
            good_answer = None
            wrong_answers = None
            yield [question, good_answer, wrong_answers]



