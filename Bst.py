import os
import pdb

class Node:
    mini = 0
    maxi = 0
    def __init__(self, data=0):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):

        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            else:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def printInorder(self):

        if self.left:
            self.left.printInorder()
        print(self.data)
        if self.right:
            self.right.printInorder()

    def printPreorder(self):

        print(self.data)
        if self.left:
            self.left.printPreorder()
        if self.right:
            self.right.printPreorder()

    def printPostorder(self):

        if self.left:
            self.left.printPostorder()
        if self.right:
            self.right.printPostorder()
        print(self.data)

    def printLevelorder(self):
        h = height(self)
        for i in range(1, h+1):
            self.printNodes(i)

    def printNodes(self, level):

        if self.data is None:
            return
        if level == 1:
                        print self.data
        elif level > 1:
            if self.left:
                self.left.printNodes(level-1)
            if self.right:
                self.right.printNodes(level-1)

    def printNode(self, level, curr_level=0):
        if self.data is None:
            return
        if curr_level == level:
            print self.data
        if self.left:
            self.left.printNode(level, curr_level-1)
        if self.right:
            self.right.printNode(level, curr_level+1)

    def printVerticalorder(self):
        self.findMinMax(self, self.mini, self.maxi)
        for i in range(self.mini, self.maxi+1):
            #pdb.set_trace()
            self.printNode(i)

    def findMinMax(self, node, min, max):
        if not node:
            return
        if node.left:
            if min-1 < self.mini:
                self.mini = min-1
            self.findMinMax(node.left, min-1, max)

        if node.right:
            if max+1 > self.maxi:
                self.maxi = max+1
            self.findMinMax(node.right, min, max+1)

    def printTopview(self):
        nodes = []
        temp = self
        pdb.set_trace()
        while(temp.left):
            temp = temp.left
            nodes.append(temp.data)

        nodes.reverse()
        nodes.append(self.data)
        temp = self
        while(temp.right):
            temp = temp.right
            nodes.append(temp.data)

        print(nodes)

def height(node):
    if node is None:
        return 0
    else:
        return max(height(node.left), height(node.right)) + 1
        
if __name__ == "__main__":
    bst = Node()
    bst.insert(10)
    bst.insert(5)
    bst.insert(15)
    bst.insert(12)
    bst.insert(17)
    bst.insert(2)
    bst.insert(7)
    bst.printVerticalorder()
    bst.printTopview()
