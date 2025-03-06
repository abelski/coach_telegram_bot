import unittest
from conversationService import answerQuestion


class TestAnswerQuestion(unittest.TestCase):
    def test_answer_user_name_question(self):
        self.assertEqual(answerQuestion("what is your name?"), "My name is Chatbot")

    def test_answer_user_age_question(self):
        self.assertEqual(answerQuestion("what is your age?"), "I am 1 year old")

    def test_answer_user_favorite_color_question(self):
        self.assertEqual(answerQuestion("what is your favorite color?"), "I like all colors")

    def test_answer_unknown_question(self):
        self.assertEqual(answerQuestion("what is your favorite food?"), "I don't understand you")

    def test_answer_empty_question(self):
        self.assertEqual(answerQuestion(""), "I don't understand you")

    def test_answer_none_question(self):
        self.assertEqual(answerQuestion(None), "I don't understand you")


if __name__ == "__main__":
    unittest.main()
