class Node(object):
    def __init__(self, elem):
        self.elem = elem
        self.next = None

class SingleCycLinkedList(object):
    def __init__(self, node=None):
        self._head = node

    def is_empty(self):
        return self._head == None

    def length(self):
        if self._head == None:
            return 0
        else:
            count = 1
            cur = self._head
            while cur.next != self._head:
                cur = cur.next
                count += 1
            return count  

    def travel(self):
        if self._head != None:
            cur = self._head
            print(cur.elem)
            while cur.next != self._head:
                cur = cur.next
                print(cur.elem)

    def add(self, item):
        node = Node(item)
        if self._head == None:
            self._head = node
            node.next = node
        else:
            # = means指向
            # 变量名means变量指向的东西
            node.next = self._head 
            self._head = node
            
    
    def append(self, item):
        node = Node(item)
        if self._head == None:
            self._head = node
            node.next = self._head
        else:
            cur = self._head 
            while cur.next != self._head:
                cur = cur.next
            node.next = self._head
            cur.next = node

    def insert(self, pos, item):
        if pos <=0:
            self.add(item)
        elif pos > self.length() -1:
            self.append(item)
        else:
            pre = self._head
            count = 0
            node = Node(item)
            while count < pos - 1:
                count += 1
                pre = pre.next
            node.next = pre.next
            pre.next = node


    
    def remove(self, item):
        if self.is_empty() == True:
            return
        cur = self._head
        if cur.next == cur:
            if cur.elem == item:
                self._head = None
        else:
            pre = None
            if cur.elem == item:
                if pre == None:
                    self._head == cur.next
            else:
                pre = cur
                cur = cur.next
                while cur != self._head:
                    if cur.elem == item:
                        if cur.next == self._head:
                            pre.next = self.head
                            
                        else:
                            pre.next = cur.next
                        break
                    else:
                        pre = cur
                        cur = cur.next

            
    def search(self, item):
        if self._head == None:
            return False
        elif self._head == item:
            return True
        else:   
            cur = self._head
            cur = cur.next
            while cur!= self._head:
                if cur.elem == item:
                    return True
                else:
                    cur = cur.next
                return False



if __name__ == "__main__":

    scl = SingleCycLinkedList()
    scl.append(1)
    scl.append(2)
    scl.append(3)
    print(scl.length())
    scl.travel()
    print(scl.search(4))
    scl.remove(2)
    scl.travel()
    print(scl.search(3))
