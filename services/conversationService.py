import services.userService as userService
import services.str_constants as constants


# function for answer user's question return string
def answerQuestion(userid: str, question: str) -> str:
    if userService.is_black_listed_user(userid):
        return constants.BLACKLISTED_USER_RESPONSE

    if question == "what is your name?":
        return "My name is Chatbot"
    elif question == "what is your age?":
        return "I am 1 year old"
    elif question == "what is your favorite color?":
        return "I like all colors"
    else:
        return "I don't understand you"
