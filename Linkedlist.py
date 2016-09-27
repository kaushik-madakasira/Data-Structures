class LinkedList():
    def __init__(self):
        self.root = None

    def insert(self, val):
        if self.root == None:
            self.root = Node(val)
            return

        temp = self.root
        while(temp.next != None):
            temp = temp.next


        temp.next = Node(val)
        return

    def delete(self, val):

        if self.root.key == val:
            temp = self.root.next
            del(self.root)
            self.root = temp
            return

        temp = self.root
        prev = None
        while(temp.next != None):
            if temp.key == val:
                prev.next = temp.next
                del(temp)
                print "Node deleted"
                return
            prev = temp
            temp = temp.next

        print "Node not found"
        return

    def printList(self):
        temp = self.root
        while(temp != None):
            print(temp.key)
            temp = temp.next

    def reverse(self):

        temp = self.root
        prev = None

        while(temp != None):
            temp_next = temp.next
            temp.next = prev
            temp.prev = temp_next
            prev = temp

            temp = temp_next
        self.root = prev

    def modify(self):
        slow_p = self.root
        fast_p = self.root

        while(fast_p.next != None and fast_p.next.next != None):
            slow_p = slow_p.next
            fast_p = fast_p.next.next

        if fast_p.next != None:
            fast_p = fast_p.next

        first_half_end = slow_p
        slow_p = slow_p.next

        temp = slow_p
        prev = None
        while(temp.next != None):
            temp_next = temp.next
            temp.next = prev
            prev = temp

            temp = temp_next


        temp.next = prev
        first_half_end.next = temp

        first = self.root
        second = temp

        while(second != None):
            first_next = first.next
            second_next = second.next

            first.next = second
            second.next = first_next

            first = first_next
            second = second_next

        first.next = None
        
        
l = LinkedList()
l.insert(10)
l.insert(20)
l.insert(30)
l.insert(40)
l.insert(50)
l.insert(60)
l.insert(70)
l.printList()
l.modify()
l.reverse()
l.printList()
l.delete(30)
l.printList()
