class Counter:
    def __init__(self, value=0):
        self.value = max(value, 0)

    def inc(self, delta=1):
        return Counter(self.value + delta)

    def dec(self, delta=1):
        return self.inc(-delta)
