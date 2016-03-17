
class TreeNode():

    def __init__(self, nodeValue):
        self.Value = nodeValue
        self.RightNode = None
        self.LeftNode = None

    def addRightNode(self, treeNode):
        if self.RightNode is None:
            self.RightNode = treeNode
        else:
            self.RightNode.insertNode(treeNode)

    def addLeftNode(self, treeNode):
        if self.LeftNode is None:
            self.LeftNode = treeNode
        else:
            self.LeftNode.insertNode(treeNode)

    def insertNode(self, treeNode):
        if treeNode.Value > self.Value:
            self.addRightNode(treeNode)
        elif treeNode.Value < self.Value:
            self.addLeftNode(treeNode)
        else:
            pass    # Or throw an exception!?

    def containsValue(self, value):
        if value == self.Value:
            return True
        elif value > self.Value:
            if self.RightNode is not None:
                return self.RightNode.containsValue(value)
        elif value <self.Value:
            if self.LeftNode is not None:
                return self.LeftNode.containsValue(value)
        return False

    def DeleteValue(self, value):
        if value == self.Value:
            return True
        if self.RightNode is not None:
            if self.RightNode.DeleteValue(value):
                rightGrandNode = self.RightNode.RightNode if self.RightNode.RightNode is not None else None
                leftGrandNode = self.RightNode.LeftNode if self.RightNode.LeftNode is not None else None
                self.RightNode = None
                if rightGrandNode is not None:
                    self.insertNode(rightGrandNode)
                if leftGrandNode is not None:
                    self.insertNode(leftGrandNode)
        if self.LeftNode is not None:
            if self.LeftNode.DeleteValue(value):
                rightGrandNode = self.LeftNode.RightNode if self.LeftNode.RightNode is not None else None
                leftGrandNode = self.LeftNode.LeftNode if self.LeftNode.LeftNode is not None else None
                self.LeftNode = None
                if rightGrandNode is not None:
                    self.insertNode(rightGrandNode)
                if leftGrandNode is not None:
                    self.insertNode(leftGrandNode)

    def printNode(self, tab):
        print(self.Value)
        if self.RightNode is None and self.LeftNode is None:
            return
        tab += 1
        print(tab*"\t", "R: " ,end="")
        if self.RightNode is not None:
            self.RightNode.printNode(tab)
        else:
            print("-")

        print(tab*"\t", "L: ", end="")
        if self.LeftNode is not None:
            self.LeftNode.printNode(tab)
        else:
            print("-")

class BST():
    def __init__(self, rootNodeValue):
        self.rootNode = TreeNode(rootNodeValue)

    def addNode(self, treeNode):
        self.rootNode.insertNode(treeNode)

    def addValue(self, value):
        treeNode = TreeNode(value)
        self.addNode(treeNode)

    def delValue(self, value):
        if value == self.rootNode.Value:
            return False
        self.rootNode.DeleteValue(value)
        # Traverse
        #Delete node
        #replace the parent's pointers

    def contains(self, value):
        return self.rootNode.containsValue(value)

    def delValueAll(self):
        pass


    def visualize(self):
        print("\t", end="")
        self.rootNode.printNode(0)

def main():
    myBST = BST(12)
    myBST.addNode(TreeNode(18))

    treeItems = [7, 16, 5, 22, 3, 6, 30, 2, 22, 23, 32, 22, 2, 9, 14, 1, 7, 7,19, 20]
    for itemValue in treeItems:
        myBST.addValue(itemValue)

    myBST.visualize()

    print(myBST.contains(7))
    print(myBST.contains(8))
    print(myBST.contains(4))
    print(myBST.contains(14))
    print(myBST.contains(55))
    print(myBST.contains(0))
    print(myBST.contains(30))
    print(myBST.contains(111))

    #myBST.delValue(22)
    myBST.delValue(18)
    myBST.visualize()

if __name__ == "__main__":
    main()

