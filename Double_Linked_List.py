# 空链表
# 只有一个节点
# 头，尾，中间


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
        return count

    def travel(self):
        if self._head == None:
            return
        cur = self._head
        while cur != None:
            print(cur.elem, end=" ")
            cur = cur.next
        print("")
    
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
            if pos >= self.length() - 1:
                count = 0
                pre = self._head
                while count != self.length -1:
                    count += 1
                    pre = pre.next
                pre.next = node
                node.next = None
                node.pre = pre

            elif pos <= 0:
                node.next = self._head
                self._head = node
            else:
                pre = self._head
                count = 0
                while count != pos - 1:
                    count += 1

                # ----@----@----@----
                #      \  /
                #        @

                # ----@    @----@---
                #     \\  //
                #        @

                node.pre = pre
                node.next = pre.next
                pre.next.pre = node
                pre.next = node


    # dll已经定义了pre，就不用另外赋值pre指向前一个节点的地址了
    def remove(self, item):
        if self.search(item) == False:
            return
        else:
            cur = self._head
            if cur.elem == item:
                if cur.next == None:
                    self._head = None
                else:
                    self._head = cur.next
                    cur.next.pre = self._head
            else:
                cur = cur.next
                while cur != None:
                    if cur.elem == item:
                        if cur.next == None:
                            cur.pre.next = None
                        else:
                            cur.pre.next = cur.next
                            cur.next.pre = cur.pre
                        return # 有while，要有return或者break，而且一定要放在最后，否则else执行不到
                    else:
                        cur = cur.next
                    
    def search(self, item):
        cur = self._head
        while cur != None:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        return False


if __name__ == "__main__":
    dll = Double_Linked_List()
    dll.append(1)
    dll.append(2)
    dll.append(3)
    dll.append(4)
    dll.travel()
    print(dll.search(4))
    print(dll.search(5))

    dll.add(0)
    dll.travel()

    print(dll.length())

    dll.insert(3, 10)
    dll.travel()

    dll.remove(1)
    dll.travel()

    dll.remove(4)
    dll.travel()

    dll.remove(10)
    dll.travel()