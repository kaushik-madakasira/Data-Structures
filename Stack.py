import pdb
import os


class Stack:
    def __init__(self):
        self.items = []

    def push(self, val):

        self.items.append(val)

    def pop(self):

        return self.items.pop()

    def top(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

    def empty(self):
        if self.size() == 0:
            return True
        else:
            return False

    def printStack(self):
        length = self.size()-1
        for i in range(length, -1, -1):
            print(self.items[i])

    def sort(self):
        if self.empty():
            return
        temp = self.pop()
        self.sort()

        self.insert(temp)
        return

    def insert(self, val):
        if self.empty():
            self.push(val)
            return

        top = self.top()
        if top < val:
            self.push(val)
            return
        else:
            temp = self.pop()
            self.insert(val)
            self.insert(temp)
            return


s = Stack()
s.push(12)
s.push(8)
s.push(2)
s.push(82)
s.push(1)
s.printStack()
s.sort()
s.printStack()
print(s.top())
print(s.pop())
print(s.top())
