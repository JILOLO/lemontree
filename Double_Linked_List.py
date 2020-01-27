class Node(object):
    def __init__(self, elem):
        self.elem = elem
        self.next = None
        self.pre = None

class Double_Linked_List(object):
    def __init__(self, node=None):
        self._head = node

    def is_empty(self):
        return self._head == None
    
    def length(self):
        if self.is_empty():
            return 0
        cur = self._head
        count = 1
        while cur.next != None:
            cur = cur.next
            count += 1

            # [] - [] - [] - [] - [] 
            # 1  2    3    4    5
            
    def travel(self):
        if self._head == None:
            return
        cur = self._head
        while cur != None:
            print(cur.elem)
            cur = cur.next
    
    def add(self, item):
        node = Node(item)
        if self.is_empty() == True:
            self._head = node
            node.next = None
        else:
            node.next = self._head
            self._head = node

    def append(self, item):
        node = Node(item)
        node.next = None
        if self._head == None:
            self._head = node
        else:
            cur = self._head
            while cur.next != None:
                cur = cur.next
            cur.next = node
            node.pre = cur

    def insert(self, pos, item):
        node = Node(item)
        if self._head == None:
            self._head = node
            node.next = None
        else:
            pre = self._head
            count = 0
            while count < pos - 1:
                count += 1
                pre = pre.next

           