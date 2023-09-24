import requests

AMOUNT = 10

CATEGORIES_NUMS = {'Sports': 'sport_and_leisure', 'Science': 'science', 'General': 'general_knowledge',
                   'Art': 'arts_and_literature', 'Society': 'society_and_culture', 'Geography': 'geography'}



URL_TEST = f"https://the-trivia-api.com/v2/questions"
PARAMS = {
    "categories": "science"
}


class GameBrain:

    def __init__(self, category):
        self.category = category
        PARAMS["categories"] = CATEGORIES_NUMS[self.category]
        respond = requests.get(URL_TEST, params=PARAMS)
        self.respond = respond.json()
        print(self.respond)



    def return_question(self):

        for i in range(AMOUNT):
            data = self.respond[i]
            question = data['question']['text']
            g_answer = data['correctAnswer']
            w_answers = data['incorrectAnswers']
            yield [question, g_answer, w_answers]



