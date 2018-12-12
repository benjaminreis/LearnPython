import random

class ListOverlap:

    def __init__(self):
        self._list_one = []
        self._list_two = []

    def GetListsLengthsFromUser(self):
        print("Welcome to \"List Overlap!\"")
        print("The length of the lists (2-100) determines the range of random numbers for each value in the list/array.")
        length = input("How long do you want the lists/arrays to be? (2-100")
        GenerateLists(self, int(length))
        FindIntersection(self)


def GenerateLists(self, length):
    for x in range(length):
        self._list_one.append(random.randint(0, length))
        self._list_two.append(random.randint(0, length))


def FindIntersection(self):
    #intersection = set(self._list_one).intersection(self._list_two)
    #leaving intersection in code to show a cuter way of doing it
    matching = []
    for a in self._list_one:
        if a in self._list_two:
            if a not in matching:
                matching.append(a)

    print("Here's your first list: " + str(self._list_one))
    print("Here's your second list: " + str(self._list_two))
    #print(intersection)
    print(matching)

