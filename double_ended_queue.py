# queue + stack 

class Deque(object):
    '''double ended queue'''
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []
    
    def add_front(self, item):
        self.items.insert(0,item)

    def add_rear(self, item):
        self.items.append(item)

    def remove_front(self):
        return self.items.pop(0)

    def remove_rear(self):
        item =self.items.pop()

    def size(self):
        return len(self.items)

    def travel(self):
        print(self.items)

if __name__ == "__main__":
    dq = Deque()
    dq.add_front(1)
    dq.add_front(2)
    dq.add_rear(3)
    dq.travel()
    dq.remove_rear()
    dq.remove_front()
    dq.travel()
    print(dq.size())

