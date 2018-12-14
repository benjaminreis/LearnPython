class ReverseWordOrder:
    def __init__(self):
        self._phrase_to_reverse = ""

    def GetPhraseToReverse(self):

        phrase = input("What phrase do you wish to reverse?")
        self._phrase_to_reverse = phrase

    def ReversePhase(self):
        temp = 1