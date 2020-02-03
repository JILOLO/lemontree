# Queue can only add element from head, remove element from tail
# FIFO first in first out
# dequeue
# enqueue

class Queue(object):
    '''Queue'''
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)
    
    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)
    
    def travel(self):
        print(self.items)

if __name__ == "__main__":
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    q.travel()
    print(q.dequeue())
    print(q.size())


