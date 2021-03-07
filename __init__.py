from mycroft import MycroftSkill, intent_file_handler


class Wheelie(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('wheelie.intent')
    def handle_wheelie(self, message):
        self.speak_dialog('wheelie')


def create_skill():
    return Wheelie()

