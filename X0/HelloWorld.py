class HelloWorld:

    def __init__(self, greeting):
        self.__greeting = greeting

    def get_greeting(self):
        return self.__greeting

    def set_greeting(self, greeting):
        self.__greeting = greeting

    def printgreeting(self):
        print(self.__greeting)
