# coding:utf-8

'''To debug'''
# choose debug point
# F5 start debug mode
# F10 go to the next point

'''Linked List 的存储格式'''
# self._head --> next --> next.next --> ...
#     |
#    None
#     |
#    node --> node = Node(elem) 

'''明确操作的对象'''
# 如果操作的对象是整个linked list，例如length，empty，add，不用考虑空linked list 的特殊情况
# 如果操作的对象是linked list里边的node，一定考虑linked list为空，里边没有Node的情况

'''while后边的条件'''
# cur != None 还是 cur.next != None 取决于你需要的操作在while里边完成
# 还是在while外边完成。如果在里边完成用前者，因为你不在意下一个是啥。
# 如果在外边完成用后者，因为执行完最后一个循环cur不能指向None，None不是Node，
# 不能执行Node相关的操作。

class Node(object):
    '''node for single link list'''
    def __init__(self, elem):
        self.elem = elem
        self.next = None

# node = Node(100)

class SingleLinkedList(object):

    def __init__(self, node=None):
        # head is a private variable
        self._head = node
    
    def is_empty(self):
        return self._head == None
    
    def length(self):
        cur = self._head
        count = 0
        while cur != None:
            count += 1
            cur = cur.next
        return count
            
    def travel(self):
        cur = self._head
        while cur != None: 
            print(cur.elem, end=" ")
            cur = cur.next
        print("")

    def add(self, elem):
        node = Node(elem)
        # cur = self._head
        # self._head = node
        # node.next = cur
        node.next = self._head
        self._head = node

    def append(self, elem):
        node = Node(elem)
        if self._head == None:
            self._head = node
        else:
            cur = self._head
            while cur.next != None: # None is no longer a node!!!
                cur = cur.next
            cur.next = node

    def insert(self, pos, elem):
        '''
        add Node(elem) AFTER the insert pos
        param:
        '''
        if pos <= 0: # cannot be negative in this case I think
            self.add(elem)
        elif pos >= self.length() - 1:
            self.append(elem)
        else:
            pre = self._head
            count = 0
            while count <= (pos-1): # if to add before pos, count < (pos-1)
                pre = pre.next
                count += 1
            node = Node(elem)
            node.next = pre.next
            pre.next = node
 
    # def remove(self, item):
    #     '''delete the first node whose value equals to item'''
    #     node = Node(item)
    #     if self._head.elem == item:
    #         add(item)
    #     else:
    #         pre = self._head
    #         while pre.next != None:
    #             if pre.next.elem == node.elem:
    #                 pre.next == pre.next.next
    #             pre = pre.next


    def remove(self, item):
        #if self._head == None:   # not necessary
        #    pass                 # not necessary
        #else:
        cur = self._head
        pre = None
        while cur != None:
            if cur.elem == item:
                if pre == None:
                    self._head = cur.next
                else:
                    pre.next = cur.next
            else:    # delete the first one. To delete all, removel else:
                pre = cur
                cur = cur.next


    def search(self, item):
        '''search if an item exists'''
        cur = self._head
        while cur != None:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        return False
        
if __name__ == "__main__":
    ll = SingleLinkedList()
    # print(ll.is_empty())
    # print(ll.length())

    # ll.append(1)
    # print(ll.is_empty())
    # print(ll.length())

    # ll.append(2)
    # ll.append(3)
    # ll.append(4)
    # print(ll.is_empty())
    # print(ll.length())

    
    ll.append(1)
    ll.append(2)
    ll.add(8)
    ll.append(3)
    ll.append(4)
    ll.append(5)  
    ll.append(6)
     # 8 1 2 3 4 5 6 

    ll.insert(-1, 9) # 98123456
    ll.insert(2, 100) # 9 8 1 100 2 3 4 5 6
    ll.insert(10, 200) # 9 8 1 100 2 3 4 5 6 200
    ll.travel()

    print(ll.search(200))

    ll.remove(3)
    ll.travel()
