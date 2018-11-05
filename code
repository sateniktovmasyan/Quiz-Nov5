#elements in linked list
class Element:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class Unsorted:
    def __init__(self):
        self.__head = None

    def setHead(self, newdata):
        self.__head = Element(newdata)

    def getHead(self, newdata):
        self.__head = Element(newdata)

    def show(self):
        printnumber = self.__head
        while printnumber is not None:
            print (printnumber.data)
            printnumber = printnumber.next

        print "*" * 20

    def append(self, newdata):
        temp = self.__head
        while temp.next is not None:
            temp = temp.next

        newnumber = Element(newdata)
        temp.next = newnumber

def main():
    numbers = Unsorted()

    numbers.setHead("2")
    numbers.append("5")
    numbers.append("4")
    numbers.append("10")

    numbers.show()


main()
