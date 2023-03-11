class HourClock:
    def __init__(self):
        self._hours = 0

    @property
    def hours(self):
        return self._hours % 12

    @hours.setter
    def hours(self, value):
        self._hours = value % 12
