class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Marge_stack:
    def __init__(self):
        self.s1 = None
        self.s2 = None
        self.temp = self.s1

    def push_s1(self,data):
        newNode = Node(data)
        newNode2 = Node(data)
        newNode.next = self.s1
        self.s1 = newNode
        newNode2.next = self.temp

    def get_first(self):
        return self.s1.data
    def get_last(self):
        return self.temp.data
if __name__ == "__main__":
    marge = Marge_stack()
    marge.push_s1(3)
    marge.push_s1(2)
    marge.push_s1(1)
    print(marge.get_first())
    print(marge.get_last())