class Queue:
    def __init__(self, cap):
        self.capacity = cap
        self.items = []

    def enqueue(self, val):
        if len(self.items) > self.capacity-1:
            print "Queue is full"
            return
        self.items.append(val)

    def dequeue(self):
        if self.isempty():
            print "Queue is empty"
            return
        val = self.items[0]
        del self.items[0]
        return val

    def peek(self):
        if self.isempty():
            print "Queue is empty"
            return
        return self.items[0]

    def isempty(self):
        if len(self.items) == 0:
            return True
        return False
        
q = Queue(3)
q.enqueue(4)
q.enqueue(5)
q.enqueue(1)
q.enqueue(9)
print(q.peek())
print(q.isempty())
q.dequeue()
print(q.peek())
#Comment 1
#Comment 2
#Comment 3
#Comment 4
