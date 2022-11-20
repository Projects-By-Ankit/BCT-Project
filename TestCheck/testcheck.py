class TestCheck:
    def __init__(self):
        self.arr = []

    def run(self):
        while True:
            if len(self.arr) > 0:
                print(self.arr.pop(0))


a = TestCheck()
print(a)

