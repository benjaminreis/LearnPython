
class ListOverlap:

    def __init__(self):
        self._list_one = []
        self._list_two = []

    def GetListsLengthsFromUser(self):
        print("Welcome to \"List Overlap!\"")
        print("The length of the lists (2-100) determines the range of random numbers for each value in the list/array.")
        length = input("How long do you want the lists/arrays to be? (2-100")
        GenerateLists(length)
        FindIntersection()


def FindIntersection(self):
    intersection = set(self._list_one).intersection(self._list_two)
    print(intersection)

    # def PrintResults(self):
    #     #TODO BEN look into doing interesection in python
    #     return ""  #http://www.practicepython.org/exercise/2014/03/05/05-list-overlap.html


def GenerateLists(self, length):
    for x in range(length):
        self._list_one.append().randint(0, length)
        self._list_two.append().randint(0, length)
