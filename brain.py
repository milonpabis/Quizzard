import requests

AMOUNT = 10
URL = f"https://opentdb.com/api.php?amount={AMOUNT}&type=multiple&category="
CATEGORIES_NUMS = {'Sports': '21', 'Mathematics': '19', 'General': '9', 'Art': '25', 'Video Games': '15',
                                   'Geography': '22'}


class GameBrain:

    def __init__(self, category):
        self.category = category
        respond = requests.get(URL + CATEGORIES_NUMS[category])
        self.respond = respond.json()["results"]
        print(self.respond)



    def return_question(self):

        for i in range(AMOUNT):
            data = self.respond[i]
            question = data['question'].replace("&#039;", "'").replace("&quot;", "\"")
            g_answer = data['correct_answer'].replace("&#039;", "'").replace("&quot;", "\"")
            w_answers = list(map(lambda x: x.replace("&#039;", "'").replace("&quot;", "\""), data['incorrect_answers']))
            yield [question, g_answer, w_answers]



