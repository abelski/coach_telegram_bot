import unittest
from services.conversation_service import answerQuestion


class TestAnswerQuestion(unittest.TestCase):
    def test_answer_user_name_question(self):
        self.assertEqual(answerQuestion("1", "what is your name?"), "My name is Chatbot")


if __name__ == "__main__":
    unittest.main()
