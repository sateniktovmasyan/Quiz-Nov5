class Element:
    def __init__(self):
        self.__data = 0
        self.__Next = None

    def getData(self):
        return self.__data

    def setData(self, data):
        self.__data = data

    def getNext(self):
        return self.__Next

    def setNext(self, Next):
        self.__Next = Next


class Unsorted:
    def __init__(self):
        self.__headNode = Element()
        self.__headNode.setNext(None)
        self.Current = self.__headNode  # set current position
        self.lastCurrent = None
        self.length = 0

    def setHead(self):
        return self.setHead

    def headNode(self):
        return self.__headNode

    def lastCurrent(self):
        return self.lastCurrent

    def __len__(self):
        return self.length

    def isEmpty(self):
        if len(self) == 0:
            return self.length

    def lastItem(self):
        self.Current=self.__headNode
        while self.Current.getNext()!=None:
            self.Current=self.Current.getNext()
        return self.Current

    def append(self, newdata):
        newElement = Element()
        newElement = setData(object)
        newElement.setNext(None)
        self.length = self.length + 1

        if self.Current == self.__headNode:
            self.__headNode.setNext(newElement)
            self.lastCurrent = self.Current
            self.Current = newElement

        else:
            self.Current.setNext(newElement)
            self.lastCurrent = self.Current
            self.Current = newElement


# def selectionsort(sorted):
#     current1 = list.headNode()
#     current = current1.getNext()
#
#     if current == 0 is False:
#         min = current
#         nextelement = current
#         beforeelement = nextelement
#         nextcurrent = current.getNext()
#
#     else:
#         if current.....

def main():
    
    sorted = Unsorted()

    sorted.setHead("2")
    sorted.append("5")
    sorted.append("4")
    sorted.append("10")




main()

