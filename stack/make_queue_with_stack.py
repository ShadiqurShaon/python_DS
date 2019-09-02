class Queue:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def enQueue(self,data):
        if len(self.s1) != 0 :
            for i in range(len(self.s1)):
                self.s2.append(self.s1.pop())
            self.s1.append(data)
            for i in range(len(self.s2)):
                self.s1.append(self.s2.pop())
        else:
            self.s1.append(data)

    def deQueue(self):
        return self.s1.pop()
if __name__ == "__main__":
    q = Queue()

    q.enQueue(1)
    q.enQueue(2)
    q.enQueue(3)
    q.enQueue(4)
    q.enQueue(5)

    print(q.deQueue())
    print(q.deQueue())
    print(q.deQueue())
    print(q.deQueue())
    print(q.deQueue())
    

