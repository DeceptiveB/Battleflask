class Game():
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2


class User():

    messages = list()

    def __init__(self, name):
        self.name = name

    def new_message(self, from_user):
        message = Message(from_user)
        messages.append(message)

class Message():

    def __init__(self, from_user):
        self.from_user = from_user
