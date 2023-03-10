class Counter:
    def __init__(self):
        self.value = 0

    def inc(self, delta=1):
        self.value += delta

    def dec(self, delta=1):
        if self.value - delta >= 0:
            self.value -= delta
        else:
            self.value = 0




