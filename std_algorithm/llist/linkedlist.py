class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, data):
        self.head = Node(data)
        
    def add(self, data):
        newnode = Node(data)
        newnode.next = self.head
        self.head = newnode
        
    # ordered add
    def add2(self, data):
        newnode = Node(data)
        cur = self.head
        prev = None
        while cur != None:
            if cur.data > data:
                if prev == None:
                    newnode.next = cur
                    self.head = newnode
                else:
                    newnode.next = cur
                    prev.next = newnode
                return
            else:
                prev = cur
                cur = cur.next
        prev.next = newnode
    
    def size(self):
        cur = self.head
        count = 0
        while cur != None:
            count += 1
            cur = cur.next
        return count
    
    def find(self, data):
        cur = self.head
        while cur != None:
            if cur.data == data:
                return True
            else:
                cur = cur.next
        return False
    
    def display(self):
        cur = self.head
        while cur != None:
            print(cur.data, end=", ")
            cur = cur.next
        print()
        
    def remove(self, data):
        cur = self.head
        prev = None
        while cur != None:
            if cur.data == data:
                if prev == None: # head == cur
                    self.head = cur.next
                else:
                    prev.next = cur.next
                break
            else:
                prev = cur
                cur = cur.next

    def removeAll(self, data):
        cur = self.head
        prev = None
        while cur != None:
            if cur.data == data:
                if prev == None: # head == cur
                    self.head = cur.next
                    cur = self.head 
                else:
                    prev.next = cur.next
                    cur = cur.next
            else:
                prev = cur
                cur = cur.next

    def removeDup(self):
        cur = self.head
        prev = None
        bucket = []
        while cur != None:
            if cur.data in bucket:
                prev.next = cur.next
                cur = cur.next
            else:
                bucket.append(cur.data)
                prev = cur
                cur = cur.next                

ll = LinkedList(12)
ll.add2(11)
ll.add2(11)
ll.add2(9)
ll.add2(6)
ll.add2(12)
ll.add2(6)
ll.add2(13)

print("size: " + str(ll.size()))
ll.display()
'''
ll = LinkedList(23)
ll.add2(4)
ll.add2(14)
ll.add2(13)
ll.add2(5)
ll.add2(6)
ll.add2(2)
ll.add2(4)
ll.add2(9)
ll.display()
'''
#ll.removeAll(12)
ll.removeDup()
print("size: " + str(ll.size()))
ll.display()
#print(ll.find(5))
#print(ll.find(90))

