# Stack is a container can only add or remove elements from tail
# LIFO, last in first out

class Stack(object):
    '''Stack'''
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []
    
    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        '''返回栈顶元素'''
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

    def travel(self):
        print(self.items)

if __name__ == "__main__":
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    print(stack.size())
    stack.travel()
    print(stack.peek())
    print(stack.pop())
    print(stack.pop())

    