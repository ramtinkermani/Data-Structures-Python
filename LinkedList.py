class ListNode():
    def __init__(self, value=None, nextNode= None):
        self.value = value
        self.nextNode = nextNode

    def addNextNode(self, nextNode):
        if self.nextNode is not None:
            raise Exception("Not the end node")
        else:
            self.nextNode = nextNode


class LinkedList():
    def __init__(self):
        self.head = ListNode()

    @property
    def length(self):
        listLength = 1;
        if self.head.value is None:
            return 0
        node = self.head
        while node.nextNode is not None:
            listLength += 1
            node = node.nextNode
        return listLength

    def insertAtHead(self, value):
        if self.head.value is None:
            self.head.value = value
            self.head.nextNode = None
        else:
            self.head = ListNode(value, self.head.nextNode)

    def insertAtEnd(self, value):
        childNode = ListNode(value)
        parentNode = self.head
        nodeAdded = False
        if self.head.value is None:
            self.head.value = value
            self.head.nextNode = None
            return
        while nodeAdded is False:
            try:
                parentNode.addNextNode(childNode)
                nodeAdded = True
            except Exception:
                parentNode = parentNode.nextNode


    def printLinkedList(self):
        if self.head.value is None:
            print("#")
        else:
            nodeToPrint = self.head
            while nodeToPrint is not None:
                print(str(nodeToPrint.value) + " -> ", end="")
                nodeToPrint = nodeToPrint.nextNode
            print("#")

def main():
    myList = LinkedList()
    list = [5,4,8,7,6,2,4,5,9]
    for i in list:
        myList.insertAtEnd(i)
    myList.printLinkedList()

    print(myList.length)

if __name__ == "__main__":
    main()