class Network:
    def __init__(self):
        self.Queue = []

    def add(self, block):
        pass

    def remove(self, block):
        pass

    def process(self, block):
        pass

    def operate(self):
        pass

    def check(self):
        while self.Queue:
            self.process(self.Queue.pop(0))
